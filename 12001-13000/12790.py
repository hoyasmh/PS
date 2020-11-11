n=int(input())
for i in range(n):
    s=list(map(int, input().split()))
    h,m,o,d=s[0]+s[4],s[1]+s[5],s[2]+s[6],s[3]+s[7]
    print(max(h,1)+5*max(m,1)+2*max(o,0)+2*d)
