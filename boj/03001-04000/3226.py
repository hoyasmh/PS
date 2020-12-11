c=0
for i in range(int(input())):
    a,b=input().split()
    t,m=map(int,a.split(':'))
    if t==18:
        c+=int(b)*10-(m+int(b))%60*5
    elif t==6:
        c+=int(b)*5+(m+int(b))%60*5
    else:
        c+=int(b)*[5,10][6<int(a.split(':')[0])<18]
print(c)
