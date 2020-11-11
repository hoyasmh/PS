l=list(map(int,input().split()))*2
def d(x,y,z,w):
    return ((x-z)**2+(y-w)**2)**.5*2
s=[d(*l[i:i+4]) for i in (0,4,8)]
print(-((l[0]-l[2])*(l[3]-l[5])==(l[1]-l[3])*(l[2]-l[4])) or max(s)-min(s))

saito
*v,=map(int,input().split());
z=0,2,4;
a,b,c=sorted(((v[i]-v[i-4])**2+(v[i+1]-v[i-3])**2)**.5for i in z);
print(-(sum(v[i]*v[i-3]-v[i+1]*v[i-4]for i in z)==0)or(c-a)*2)
