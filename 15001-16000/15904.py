s=input()
u='UCPC'
n=0
for i in s:
    if i==u[n]:
        n+=1
        if n==4:
            print('I love UCPC')
            break
else:
    print('I hate UCPC')
