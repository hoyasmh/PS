n=int(input())
l=sorted(list(map(int,input().split())))
print(2*sum([l[i]*(2*(i)-n+1) for i in range(n)]))
