from collections import deque
input()
a=deque(map(int,input().split()))
b=deque(map(int,input().split()))
while a and b:
    if a[0]<b[0]:
        print(a.popleft(),end=' ')
    else:
        print(b.popleft(),end=' ')
print(*a if len(b)==0 else b)

input()
print(" ".join(sorted(input().split()+input().split(),key=int)))

f=lambda:[*map(int,input().split())];input();print(*sorted(f()+f()))
