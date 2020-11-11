for i in [0]*int(int(input())):
    l=list(input().split())
    l[0]=float(l[0])
    for j in range(1,len(l)):
        if l[j]=='@':
            l[0]*=3
        elif l[j]=='%':
            l[0]+=5
        else:
            l[0]-=7
        print(l[0])
    print('%.2f' % l[0])
