h=10
l=list(input())
for i in range(1,len(l)):
    if l[i]==l[i-1]:
        h+=5
    else:
        h+=10
print(h)
    
