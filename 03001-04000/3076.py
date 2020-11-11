m,n=map(int,input().split())
a,b=map(int,input().split())
for i in range(m*a):
    print((('{}'.format('.X'[i%(a*2)<a])*b+'{}'.format('X.'[i%(a*2)<a])*b)*6)[:n*b])
