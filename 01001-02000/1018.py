m,n=map(int,input().split())
l=[input() for i in range(m)]
M=64
for i in range(m-7):
    for j in range(n-7):
        c=0
        for k in range(8):
            for t in range(8):
                if l[i+k][j+t]=='WB'[(k+t)%2]:
                    c+=1
        M=min(c,64-c,M)
print(M)
