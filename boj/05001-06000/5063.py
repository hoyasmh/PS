n=int(input())
for i in range(n):
    r,e,c=map(int, input().split())
    a=e-c
    if a>r:
        print('advertise')
    elif a==r:
        print('does not matter')
    else:
        print('do not advertise')
