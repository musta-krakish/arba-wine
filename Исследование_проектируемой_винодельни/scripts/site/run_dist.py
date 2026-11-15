import json,re
from dist import *
out={}
subs=json.load(open('subs_all.json'))
roads=json.load(open('roads.json'))['elements']
lines=json.load(open('lines.json'))['elements']
lu={k:json.load(open(f'lu_{k}.json'))['elements'] for k in 'ABCD'}
ww=[e for k in lu for e in lu[k] if 'waterway' in e['tags'] and e.get('geometry')]
res=[e for k in lu for e in lu[k] if e['tags'].get('landuse')=='residential' and e.get('geometry')]
np_=json.load(open('np.json'))['elements']
haz={}
for L,nm in [(0,'Сель 500 м'),(1,'Сель 100 м'),(2,'Оползень 500 м'),(3,'Оползень 100 м')]:
    haz[nm]=json.load(open(f'selg_{L}.json'))['features']
haz['Паводок (опасн. уровень)']=json.load(open('pavg.json'))['features']
for s,p in SITES.items():
    print('=====',s,p)
    # substations
    ds=sorted((hav(p,(x[1],x[2])),x) for x in subs)[:4]
    for d,x in ds: print(f'  ПС {d:.2f} км',x)
    # roads by ref/name
    best={}
    for e in roads:
        t=e['tags'];g=[(q['lat'],q['lon']) for q in e['geometry']]
        key=(t.get('highway'),t.get('ref') or t.get('name'))
        d=lined(p,g)[0]
        if key not in best or d<best[key][0]: best[key]=(d,t.get('name'))
    for k,v in sorted(best.items(),key=lambda x:x[1][0])[:5]: print(f'  дорога {v[0]:.2f} км',k,v[1])
    # waterways
    bw={}
    for e in ww:
        t=e['tags'];nm=t.get('name');
        if not nm: continue
        g=[(q['lat'],q['lon']) for q in e['geometry']]
        d=lined(p,g)[0]; key=(t['waterway'],nm)
        if key not in bw or d<bw[key]: bw[key]=d
    for k,v in sorted(bw.items(),key=lambda x:x[1])[:6]: print(f'  вода {v:.2f} км',k)
    # residential nearest edge
    br=[]
    for e in res:
        g=[(q['lat'],q['lon']) for q in e['geometry']]
        d=0 if inpoly(p,g) else lined(p,g)[0]
        br.append((d,e['tags'].get('name','(без имени)')))
    br.sort(); print('  жильё',[(round(d,2),n) for d,n in br[:3]])
    # power lines
    bl=[]
    for e in lines:
        g=[(q['lat'],q['lon']) for q in e['geometry']]
        bl.append((lined(p,g)[0],e['tags'].get('power'),e['tags'].get('voltage'),e['id']))
    bl.sort(key=lambda x:x[0]); print('  ЛЭП OSM',[(round(a,2),b,c,i) for a,b,c,i in bl[:3]])
    # NP
    for e in np_:
        dm=1e9
        for m in e['members']:
            if m.get('geometry'):
                g=[(q['lat'],q['lon']) for q in m['geometry']]
                dm=min(dm,lined(p,g)[0])
        print(f'  ООПТ {dm:.2f} км',e['tags'].get('name'))
    for nm,F in haz.items():
        dm=1e9;who=None
        for f in F:
            for r in f['geometry']['rings']:
                g=[(y,x) for x,y in r]
                d=0 if inpoly(p,g) else lined(p,g)[0]
                if d<dm: dm=d;who={k:v for k,v in f['attributes'].items() if k.lower() in ('bassein_reki','np','название_гидропоста')}
        print(f'  {nm}: {dm:.2f} км',who)
    print('  Алматы (центр, по прямой) %.1f км'%hav(p,(43.2383,76.9453)))
