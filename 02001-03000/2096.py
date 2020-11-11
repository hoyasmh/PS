# a=[0]*5
# c=[0]*5
# b=[0]*5
# d=[0]*5
# for i in range(int(input())):
#     l=list(map(int,input().split()))
#     for j in range(3):
#         c[j+1]=max(l[j]+a[j],l[j]+a[j+1],l[j]+a[j+2])
#         d[j+1]=min(l[j]+b[j],l[j]+b[j+1],l[j]+b[j+2])
#     a,b=c[:],d[:]
#     print(a,b)
# print(max(a),min(b[1:4]))

import sys
a=[0]*3
c=[0]*3
b=[0]*3
d=[0]*3
for i in range(int(input())):
    l=list(map(int,sys.stdin.readline().split()))
    for j in range(3):
        c[j]=l[j]+max(a[max(0,j-1):j+2])
        d[j]=l[j]+min(b[max(0,j-1):j+2])
    a,b=c[:],d[:]
print(max(a),min(b))

saito 풀이
M=m=[0]*3
for _ in[0]*int(input()):x,y,z=map(int,input().split());M,m=([f(v[:2])+x,f(v)+y,f(v[1:])+z]for f,v in[(max,M),(min,m)])
print(max(M),min(m))
