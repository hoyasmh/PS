n=int(input())
for i in range(n):
    s=sum([ord(i)-64 for i in ''.join(input().split(' '))])
    if s==100:
        print('PERFECT LIFE')
    else:
        print(s)
