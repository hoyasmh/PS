n=int(input())
for i in range(n):
    a, b = map(int, input().split())
    l=a*b
    while b%a !=0:
        a, b = b%a, a
    print(l//a)    
