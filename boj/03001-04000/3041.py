l=[input() for i in range(4)]
c=0
for i in range(15):
    for j in range(4):
        d=chr(i+65)
        if d in l[j]:
            c+=abs(i//4-j)+abs(i%4-l[j].index(d))
print(c)
