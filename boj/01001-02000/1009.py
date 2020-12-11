n=int(input())
for i in range(n):
    a, b = map(int ,input().split())
    a, b= a%10, b%4+4
    if a**b%10==0:
        print(10)
    else:
        print(a**b%10)
