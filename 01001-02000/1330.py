a,b=map(int,input().split())
print(['==','<>'[a>b]][len({a,b})-1])
