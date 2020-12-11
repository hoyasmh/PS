from math import factorial as fact
c = int(input())
for i in range(c):
    m, n = map(int ,input().split())
    print(fact(n)//fact(m)//fact(n-m))
