n=int(input())
l=list(map(int,input().split()))
if n==1:
	print('B')
elif n==2 or l[0]==l[1]:
	print(l[0] if l[0]==l[1] else 'A')
else:
	p,q=(l[-1]-l[0])*(l[2]-l[1]),l[1]-l[0]
	print([p//q+l[1],'B'][p%q!=0])
