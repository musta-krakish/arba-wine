import sys
from PIL import Image,ImageDraw,ImageFont
F=ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf",13)
FB=ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf",20)
# name, bbox lon0,lat0,lon1,lat1, points
J={
 'T1':((77.615,43.425,77.695,43.485),[('В',43.460,77.645),('З',43.457,77.636),('Arba',43.4273,77.6217)]),
 'T2':((77.48,43.46,77.56,43.52),[('В',43.4827,77.5307),('З',43.4905,77.5200)]),
 'S':((78.25,43.535,78.33,43.595),[('В',43.5607,78.298),('З',43.567,78.289),('ПС',43.5837,78.265)]),
 'U':((79.46,43.635,79.54,43.695),[('В',43.673,79.505),('З',43.6607,79.5067)]),
}
out=sys.argv[1]
for n,(b,pts) in J.items():
    im=Image.open(f'img/{n}.jpg').convert('RGB');W,H=im.size;d=ImageDraw.Draw(im)
    for lab,la,lo in pts:
        x=(lo-b[0])/(b[2]-b[0])*W;y=(b[3]-la)/(b[3]-b[1])*H
        if not(0<=x<W and 0<=y<H): continue
        if lab=='В':
            # 54.75 ha square ~740 m
            import math
            hx=370/(111320*math.cos(math.radians(la)))/(b[2]-b[0])*W; hy=370/110570/(b[3]-b[1])*H
            d.rectangle([x-hx,y-hy,x+hx,y+hy],outline=(255,255,0),width=3)
        elif lab=='З':
            hx=60/(111320*math.cos(math.radians(la)))/(b[2]-b[0])*W; hy=60/110570/(b[3]-b[1])*H
            d.rectangle([x-hx,y-hy,x+hx,y+hy],outline=(255,0,0),width=3)
        else:
            d.ellipse([x-8,y-8,x+8,y+8],outline=(0,255,255),width=3)
        d.text((x+10,y+10),lab,fill=(255,255,0),font=FB)
    d.rectangle([0,H-22,W,H],fill=(0,0,0))
    d.text((6,H-18),f'Площадка {n}. Esri World Imagery (c) Esri, Maxar, Earthstar Geographics. Жёлтый: условно 54,75 га; красный: условно завод ~1,4 га. Не кадастр.',fill=(255,255,255),font=F)
    im.save(f'{out}/site_{n}_esri.jpg',quality=88)
print('ok')
