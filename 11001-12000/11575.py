for i in range(int(input())):
    a,b=map(int,input().split())
    for i in input():
        print(chr(((ord(i)-65)*a+b)%26+65),end='')
    print('')
