input()
l=list(map(int,input().split()))
y,m=0,0
for i in l:
    y+=10*((i+1)//30+bool((i+1)%30))
    m+=15*((i+1)//60+bool((i+1)%60))
if y==m:
    print('Y M {}'.format(min(y,m)))
else:
    print('YM'[m<y], min(y,m))
