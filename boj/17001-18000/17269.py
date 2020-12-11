t=str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ','32124313113132122212111221')
m=min(map(int,input().split()))
a,b=input().split()
s=''.join([i+j for i,j in zip(a,b)])+a[m:]+b[m:]
l=[int(i) for i in s.translate(t)]
while len(l)>2:
    l=[(l[i]+l[i+1])%10 for i in range(len(l)-1)]
print('{}%'.format(int(str(l[0])+str(l[1]))))
