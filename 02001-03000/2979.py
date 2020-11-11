import collections
a=list(map(int, input().split()))
l=[]
for i in range(3):
    n,m=map(int, input().split())
    l+=[j for j in range(n,m)]
s=list(collections.Counter(l).values())
print(sum([k*a[k-1]*s.count(k) for k in range(1,4)]))

# x=list(map(int,input().split()));x,t,p=[0]+x,[0]*101,0
# for i in range(3):
#  s,e=map(int,input().split())
#  for i in range(s,e):t[i]+=1
# for i in t:p+=x[i]*i
# print(p)
