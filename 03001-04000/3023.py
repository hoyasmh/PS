r,c=map(int,input().split())
l=[]
for i in range(r):
    s=input()
    l.append(s+s[::-1])
l=l+l[::-1]
a,b=map(int,input().split())
for j in range(r*2):
    if j+1==a:
        l[j]=l[j][:b-1]+'.#'[l[j][b-1]=='.']+l[j][b:]
    print(l[j])
