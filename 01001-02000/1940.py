n,m=int(input()),int(input())
l=sorted(list(map(int,input().split())))
print(sum([1 for i in l if i<(m+1)//2 and m-i in l]))
