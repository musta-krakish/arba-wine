import json,math,sys,datetime as dt
d=json.load(open(sys.argv[1]))['properties']['parameter']
M=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
days=[31,28,31,30,31,30,31,31,30,31,30,31]
lat=math.radians(43.43); z=830
def es(T): return 0.6108*math.exp(17.27*T/(T+237.3))
ETo={};P={};RHmin={}
for i,m in enumerate(M):
    T=d['T2M'][m]; R=d['T2M_RANGE'][m]; Tx=T+R/2; Tn=T-R/2
    Pa=d['PS'][m]; g=0.000665*Pa; u2=d['WS2M'][m]; Rs=d['ALLSKY_SFC_SW_DWN'][m]
    esv=(es(Tx)+es(Tn))/2; q=d['QV2M'][m]/1000; ea=q*Pa/(0.622+0.378*q)
    D=4098*es(T)/(T+237.3)**2; J=[15,46,74,105,135,162,198,228,258,288,318,344][i]
    dr=1+0.033*math.cos(2*math.pi*J/365); dec=0.409*math.sin(2*math.pi*J/365-1.39)
    ws=math.acos(-math.tan(lat)*math.tan(dec))
    Ra=24*60/math.pi*0.082*dr*(ws*math.sin(lat)*math.sin(dec)+math.cos(lat)*math.cos(dec)*math.sin(ws))
    Rso=(0.75+2e-5*z)*Ra
    Rnl=4.903e-9*((Tx+273.16)**4+(Tn+273.16)**4)/2*(0.34-0.14*math.sqrt(ea))*(1.35*min(Rs/Rso,1)-0.35)
    Rn=0.77*Rs-Rnl
    ETo[i+1]=(0.408*D*Rn+g*900/(T+273)*u2*(esv-ea))/(D+g*(1+0.34*u2))
    P[i+1]=d['PRECTOTCORR'][m]*days[i]; RHmin[i+1]=100*ea/es(Tx)
    print(m, 'Tx=%.1f Tn=%.1f ea=%.2f RHmin=%.0f u2=%.2f ETo=%.2f mm/d (%.0f mm) P=%.0f'%(Tx,Tn,ea,RHmin[i+1],u2,ETo[i+1],ETo[i+1]*days[i],P[i+1]))
# Kc mid adjust (FAO-56 eq.62), h=1.8 m, July-Aug RHmin
u2m=(d['WS2M']['JUL']+d['WS2M']['AUG'])/2; rh=(RHmin[7]+RHmin[8])/2
Kmid=0.70+(0.04*(u2m-2)-0.004*(rh-45))*(1.8/3)**0.3
print('RHmin mid=%.1f u2=%.2f Kc_mid_adj=%.3f'%(rh,u2m,Kmid))
# stages: budbreak 15 Apr; 30/60/40/80
start=dt.date(2026,4,15); L=[30,60,40,80]
def kc(day):
    n=(day-start).days
    if n<0: return None
    if n<L[0]: return 0.30
    if n<L[0]+L[1]: return 0.30+(Kmid-0.30)*(n-L[0])/L[1]
    if n<sum(L[:3]): return Kmid
    if n<sum(L): return Kmid+(0.45-Kmid)*(n-sum(L[:3]))/L[3]
    return None
end_irr=dt.date(2026,9,30)
# RDI factors (assumption): 1.0 until fruit set (~15 Jun), 0.6 fruit set->veraison (~31 Jul), 0.8 veraison->stop
def rdi(day):
    if day<dt.date(2026,6,15): return 1.0
    if day<dt.date(2026,8,1): return 0.6
    return 0.8
mon={}
day=start
while day<=end_irr:
    k=kc(day); e=ETo[day.month]*k
    m=mon.setdefault(day.month,{'ETc':0,'ETc_rdi':0,'days':0,'kcs':[]})
    m['ETc']+=e; m['ETc_rdi']+=e*rdi(day); m['days']+=1; m['kcs'].append(k)
    day+=dt.timedelta(1)
tot=dict(ETc=0,rdi=0,Pe=0,In=0,In_rdi=0)
print('month days Kc_avg ETo_mm ETc_mm P_mm Pe_mm In_full In_rdi')
for mo,m in mon.items():
    frac=m['days']/days[mo-1]; Pm=P[mo]*frac
    Pe=Pm*(125-0.2*Pm)/125 if Pm<250 else 125+0.1*Pm
    # Pe limited: drip, assume only 50% of rain useful? keep USDA SCS; also limit Pe<=ETc
    In=max(m['ETc']-Pe,0); Inr=max(m['ETc_rdi']-Pe,0)
    print(mo,m['days'],'%.2f'%(sum(m['kcs'])/len(m['kcs'])),'%.0f'%(ETo[mo]*m['days']),'%.0f'%m['ETc'],'%.0f'%Pm,'%.0f'%Pe,'%.0f'%In,'%.0f'%Inr)
    tot['ETc']+=m['ETc'];tot['rdi']+=m['ETc_rdi'];tot['Pe']+=Pe;tot['In']+=In;tot['In_rdi']+=Inr
print({k:round(v) for k,v in tot.items()})
Ea=0.90
for nm,v in [('full',tot['In']),('rdi',tot['In_rdi'])]:
    print(nm,'net %.0f mm = %.0f m3/ha; gross %.0f m3/ha; 54.75ha: %.0f m3'%(v,v*10,v*10/Ea,v*10/Ea*54.75))
peak=ETo[7]*Kmid
print('peak July ETc %.2f mm/d; gross %.2f; m3/d total %.0f'%(peak,peak/Ea,peak/Ea*10*54.75))
