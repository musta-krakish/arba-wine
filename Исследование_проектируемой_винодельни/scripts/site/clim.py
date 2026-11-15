import json,datetime as dt,statistics as st
for n in ['T1','T2','S','U','ARBA']:
    d=json.load(open(f'clim/{n}.json'));D=d['daily']
    days=[dt.date.fromisoformat(t) for t in D['time']]
    tm,tn,tx,pr,et=D['temperature_2m_mean'],D['temperature_2m_min'],D['temperature_2m_max'],D['precipitation_sum'],D['et0_fao_evapotranspiration']
    Y={}
    for i,day in enumerate(days): Y.setdefault(day.year,[]).append(i)
    sat=[];gdd=[];hug=[];ffp=[];lsf=[];fsf=[];per10=[];pann=[];pveg=[];etveg=[];hot=[];late2=[]
    for y,idx in Y.items():
        sat.append(sum(tm[i] for i in idx if tm[i]>10))
        gdd.append(sum(max(tm[i]-10,0) for i in idx if 4<=days[i].month<=10))
        hug.append(1.04*sum(max(((tm[i]-10)+(tx[i]-10))/2,0) for i in idx if 4<=days[i].month<=9))
        spring=[i for i in idx if days[i].month<=6 and tn[i]<=0]; autumn=[i for i in idx if days[i].month>=7 and tn[i]<=0]
        ls=days[spring[-1]] if spring else None; fs=days[autumn[0]] if autumn else None
        if ls and fs: ffp.append((fs-ls).days-1); lsf.append(ls.timetuple().tm_yday); fsf.append(fs.timetuple().tm_yday)
        # period with 5-day running mean >10
        rm=[sum(tm[idx[k]] for k in range(j-2,j+3))/5 if 2<=j<len(idx)-2 else None for j in range(len(idx))]
        ab=[j for j,v in enumerate(rm) if v is not None and v>10]
        if ab: per10.append(ab[-1]-ab[0]+1)
        pann.append(sum((pr[i] or 0) for i in idx)); pveg.append(sum((pr[i] or 0) for i in idx if 4<=days[i].month<=9)); etveg.append(sum((et[i] or 0) for i in idx if 4<=days[i].month<=9))
        hot.append(sum(1 for i in idx if tx[i]>=35))
        late2.append(any(tn[i]<=-2 for i in idx if (days[i].month==4 and days[i].day>=20) or days[i].month==5))
    # winter minima: winter = Nov(y-1)..Mar(y)
    wmin=[]
    for y in range(1996,2025):
        v=[tn[i] for i,day in enumerate(days) if (day.year==y-1 and day.month>=11) or (day.year==y and day.month<=3)]
        wmin.append(min(v))
    absmin=min(tn); iam=tn.index(absmin)
    f=lambda x:dt.date(2001,1,1)+dt.timedelta(days=round(x)-1)
    print(f"{n}: высота DEM {d['elevation']} м; узел {d['latitude']},{d['longitude']}")
    print(f"  ΣT>10 ср {st.mean(sat):.0f} (мин {min(sat):.0f}, макс {max(sat):.0f}); Winkler GDD ср {st.mean(gdd):.0f}; Huglin {st.mean(hug):.0f}")
    print(f"  период с T>10 (скольз.5сут) ср {st.mean(per10):.0f} сут; безморозный ср {st.mean(ffp):.0f} сут (мин {min(ffp)})")
    print(f"  последн. весенний заморозок ≤0 ср {f(st.mean(lsf)):%d.%m}, самый поздний {f(max(lsf)):%d.%m}; первый осенний ср {f(st.mean(fsf)):%d.%m}, самый ранний {f(min(fsf)):%d.%m}")
    print(f"  лет с заморозком ≤-2 после 20.04: {sum(late2)}/{len(late2)}")
    print(f"  абс. мин {absmin} ({days[iam]}); ср. из годовых абс. минимумов зимы {st.mean(wmin):.1f}; зим ≤-20: {sum(1 for w in wmin if w<=-20)}/{len(wmin)}, ≤-25: {sum(1 for w in wmin if w<=-25)}")
    print(f"  осадки год {st.mean(pann):.0f} мм, апр-сен {st.mean(pveg):.0f} мм; ET0 апр-сен {st.mean(etveg):.0f} мм; дефицит {st.mean(etveg)-st.mean(pveg):.0f} мм; дней Tmax≥35: {st.mean(hot):.1f}")
