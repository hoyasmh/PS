l=[1]
for k in range(int(input())):
    n=int(input())
    if n>len(l):
        for i in range(len(l),n):
            l.append(l[-1]*(i+1))
    for j in str(l[n-1])[::-1]:
        if j!='0':
            print(j)
            break
