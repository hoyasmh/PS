l=set()
y=(i for i in input().split())
for i in y:
    if i not in l:
        print(i,end=' ')
        l.add(i)
