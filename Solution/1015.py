사이토2000
n,m=map(int,input().split())
r=[0]*m
a=0
exec('t=[]\nfor v,d in zip(r,map(int,input())):c=t and-~min(v,w,b)*d or d;t+=c,;a=max(a,c*c);b=c;w=v\nr=t;'*n)
print(a)
큐브러버
n,m=map(int,input().split())
d=[0]*m
r=0
for i in range(n):
	s=input()
	a=[[0,0]]
	for j in range(m):
		d[j]+=1
		if s[j]=='0':
			d[j]=0
		while a[len(a)-1][0]>d[j]:
			r=max(r,min(j-a[len(a)-2][1],a[len(a)-1][0])**2)
			a.pop()
		a.append([d[j],j+1])
	while a[len(a)-1][0]:
		r=max(r,min(m-a[len(a)-2][1],a[len(a)-1][0])**2)
		a.pop()
print(r)
