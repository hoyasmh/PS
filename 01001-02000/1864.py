s='/-\\(@?>&%'
n=input()
while '#'!=n:
    m=0
    for i in range(len(n)):
        m+=(s.index(n[i])-1)*8**(len(n)-i-1)
    print(m)
    n=input()
