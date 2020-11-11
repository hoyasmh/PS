c=0
for i in range(int(input())):
    l=list(input())
    k=1
    for j in range(1,len(l)):
        if l[j]!=l[j-1]:
            k+=1
    if len(set(l))==k:
        c+=1
print(c)

    
