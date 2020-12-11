for i in range(int(input())):
    s=input()
    m=0
    while s!='6174':
        s=''.join(sorted([j for j in s]))
        s=str(int(s[::-1])-int(s)).zfill(4)
        m+=1
    print(m)
