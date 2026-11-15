import json,math,urllib.request,time
S={'T1':(43.460,77.645),'T2':(43.4827,77.5307),'S':(43.5607,78.298),'U':(43.673,79.505),'ARBA':(43.4273,77.6217)}
res={}
for n,(la,lo) in S.items():
    pts=[];step=150
    for i in range(-3,4):
        for j in range(-3,4):
            pts.append((la+i*step/110570,lo+j*step/(111320*math.cos(math.radians(la))),i*step,j*step))
    url='https://api.open-meteo.com/v1/elevation?latitude='+','.join('%.5f'%p[0] for p in pts)+'&longitude='+','.join('%.5f'%p[1] for p in pts)
    e=json.load(urllib.request.urlopen(url,timeout=60))['elevation']
    # least squares plane z=a+b*x+c*y
    X=[p[3] for p in pts];Y=[p[2] for p in pts];n_=len(e)
    mx=sum(X)/n_;my=sum(Y)/n_;mz=sum(e)/n_
    b=sum((x-mx)*(z-mz) for x,z in zip(X,e))/sum((x-mx)**2 for x in X)
    c=sum((y-my)*(z-mz) for y,z in zip(Y,e))/sum((y-my)**2 for y in Y)
    sl=math.hypot(b,c); asp=(math.degrees(math.atan2(-b,-c))+360)%360  # direction of downslope (0=N)
    print(n,'центр',e[24],'мин',min(e),'макс',max(e),'уклон %.1f%% (%.2f°)'%(sl*100,math.degrees(math.atan(sl))),'падение к азимуту %.0f°'%asp)
    time.sleep(1)
