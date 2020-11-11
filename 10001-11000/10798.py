l=[input() for i in range(5)]
while l:
    a=l.pop(0)
    if len(a)>0:
        print(a[0],end='')
        l.append(a[1:])
