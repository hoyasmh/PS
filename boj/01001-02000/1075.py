n=int(input()[:-2]+'00')
f=int(input())
if n%f:
    print(str(100+f-n%f)[1:])
else:
    print('00')
