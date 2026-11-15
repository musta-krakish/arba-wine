import json,sys,math
from collections import Counter
def area(g):
    if len(g)<3: return 0
    lat0=sum(p['lat'] for p in g)/len(g)
    xs=[p['lon']*111320*math.cos(math.radians(lat0)) for p in g]; ys=[p['lat']*110540 for p in g]
    return abs(sum(xs[i]*ys[i-1]-xs[i-1]*ys[i] for i in range(len(g))))/2/1e4
for n in sys.argv[1:]:
    d=json.load(open(f'lu_{n}.json'))
    print('=====',n)
    big=[];ww=Counter()
    for e in d['elements']:
        t=e['tags'];g=e.get('geometry')
        if 'waterway' in t:
            ww[(t['waterway'],t.get('name'))]+=1; continue
        if not g: continue
        a=area(g); c=(sum(p['lat'] for p in g)/len(g),sum(p['lon'] for p in g)/len(g))
        big.append((round(a,1),t.get('landuse'),t.get('crop',''),t.get('name',''),round(c[0],4),round(c[1],4),e['id']))
    tot=Counter()
    for b in big: tot[b[1]]+=b[0]
    print({k:round(v) for k,v in tot.items()})
    for b in sorted(big,reverse=True)[:25]: print(b)
    print([k for k,v in ww.most_common(40) if k[1]])
