n=int(input())
l=list(map(int, input().split()))
c=int(input())
s=0
while s!=sum(l):
    s=sum(l)
    l=[i for i in l if i>c//len(l)]
    c=c-(s-sum(l))
print(c//len(l))
