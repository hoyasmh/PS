n=int(input())
l=sorted(list(map(int,input().split())))[::-1]+[0]
for i in range(n):
    if l[i]>=i+1 and i+1>=l[i+1]:
        print(i+1)
        break
else:
    print(0)
