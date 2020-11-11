l=sorted(list(map(int,input().split())))
while sum(l)>0:
    if l[2]>=l[1]+l[0]:
        print('Invalid')
    else:
        print(['Equilateral','Isosceles','Scalene'][len(set(l))-1])
    l=sorted(list(map(int,input().split())))
