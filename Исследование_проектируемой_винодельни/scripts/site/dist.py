import json,math
R=6371.0088
def hav(a,b):
    la1,lo1=map(math.radians,a);la2,lo2=map(math.radians,b)
    h=math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
def segd(p,a,b):
    # local equirectangular projection around p, km
    k=math.cos(math.radians(p[0]))
    P=(0,0);A=((a[1]-p[1])*111.32*k,(a[0]-p[0])*110.57);B=((b[1]-p[1])*111.32*k,(b[0]-p[0])*110.57)
    dx,dy=B[0]-A[0],B[1]-A[1];L=dx*dx+dy*dy
    t=0 if L==0 else max(0,min(1,-(A[0]*dx+A[1]*dy)/L))
    x,y=A[0]+t*dx,A[1]+t*dy
    return math.hypot(x,y),(p[0]+y/110.57,p[1]+x/(111.32*k))
def lined(p,pts):
    best=(1e9,None)
    for i in range(len(pts)-1):
        d=segd(p,pts[i],pts[i+1])
        if d[0]<best[0]: best=d
    return best
def inpoly(p,ring):
    y,x=p;c=False
    for i in range(len(ring)):
        y1,x1=ring[i];y2,x2=ring[i-1]
        if (y1>y)!=(y2>y) and x<(x2-x1)*(y-y1)/(y2-y1)+x1: c=not c
    return c
SITES={
 'T1_vin':(43.460,77.645),'T1_zav':(43.457,77.636),
 'T2_vin':(43.4827,77.5307),'T2_zav':(43.4905,77.5200),
 'S_vin':(43.5607,78.298),'S_zav':(43.567,78.289),
 'U_vin':(43.673,79.505),'U_zav':(43.6607,79.5067),
 'ARBA':(43.4273,77.6217)}
