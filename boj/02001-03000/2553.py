n=1
for i in range(1,int(input())+1):
    n*=i
for j in str(n)[::-1]:
    if j!='0':
        print(j)
        break
