a,b=map(int,input().split())
while b<101 and a>=b*(b-1)//2:
    n=a-b*(b-1)//2
    if n%b==0:
        print(*[n//b+j for j in range(b)])
        exit()
    b+=1
print(-1)

N,L=map(int,input().split());t=[-1]
for i in range(L,101):
 if (N-i*(i+1)/2)%i == 0:
  a=int(N/i-(i-1)/2)
  if a>-1:t=range(a,a+i);break
print(*t)
