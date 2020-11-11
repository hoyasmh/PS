for i in range(int(input())):
    n=int(input())-1
    l=[]
    for j in range(n//2):
        l.append(str(j+1)+' '+str(n-j))
    print('Pairs for {}:'.format(n+1),(', ').join(l))
