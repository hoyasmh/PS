n=int(input())
while n!='0':
    l=[]
    d={}
    for i in range(n):
        s=input()
        l.append(s.upper())
        d[s.upper()]=s
    print(d[sorted(l)[0]])
    n=int(input())
