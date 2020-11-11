s=input()
while s!='0':
    l=s.split()
    print(l[1],end=' ')
    for i in range(int(l[0])-1):
        if l[i+1]!=l[i+2]:
            print(l[i+2],end=' ')
    print('$')
    s=input()
