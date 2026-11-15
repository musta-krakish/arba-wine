import json,math,sys
d=json.load(open(sys.argv[1]))['properties']['parameter']
M=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
days=[31,28,31,30,31,30,31,31,30,31,30,31]
lat=math.radians(43.43); z=float(sys.argv[2]) if len(sys.argv)>2 else 830
J=[15,46,74,105,135,162,198,228,258,288,318,344]
def es(T): return 0.6108*math.exp(17.27*T/(T+237.3))
tot=0;out=[]
for i,m in enumerate(M):
    T=d['T2M'][m]; R=d['T2M_RANGE'][m]; Tx=T+R/2; Tn=T-R/2
    P=d['PS'][m]; g=0.000665*P
    u2=d['WS2M'][m]; Rs=d['ALLSKY_SFC_SW_DWN'][m]
    esv=(es(Tx)+es(Tn))/2; ea=esv*d['RH2M'][m]/100
    # RH2M is mean RH relative to es(Tmean)? use ea from QV2M instead
    q=d['QV2M'][m]/1000; ea=q*P/(0.622+0.378*q)
    D=4098*es(T)/(T+237.3)**2
    dr=1+0.033*math.cos(2*math.pi*J[i]/365); dec=0.409*math.sin(2*math.pi*J[i]/365-1.39)
    ws=math.acos(-math.tan(lat)*math.tan(dec))
    Ra=24*60/math.pi*0.082*dr*(ws*math.sin(lat)*math.sin(dec)+math.cos(lat)*math.cos(dec)*math.sin(ws))
    Rso=(0.75+2e-5*z)*Ra; Rns=0.77*Rs
    s=4.903e-9; Rnl=s*((Tx+273.16)**4+(Tn+273.16)**4)/2*(0.34-0.14*math.sqrt(ea))*(1.35*min(Rs/Rso,1)-0.35)
    Rn=Rns-Rnl
    ET=(0.408*D*Rn+g*900/(T+273)*u2*(esv-ea))/(D+g*(1+0.34*u2))
    hg=0.0023*(T+17.8)*math.sqrt(R)*Ra*0.408
    pr=d['PRECTOTCORR'][m]*days[i]
    out.append((m,round(T,1),round(ea,2),round(Rs,1),round(ET,2),round(ET*days[i]),round(hg,2),round(pr)))
    tot+=ET*days[i]
for o in out: print(o)
print('annual',round(tot))
