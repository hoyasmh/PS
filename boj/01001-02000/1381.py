import sys
n, k = map(int, sys.stdin.readline().split())
l = sorted([tuple(map(int, sys.stdin.readline().split())) for i in range(n)], key = lambda x : (-x[0], x[1]))
p = 1
for i in range(k):
    p *= (1 - l[i][1] / 100)
ans = round((1 - p) * 100, 3)
if ans < 0.001:
    print("GG")
else:
    print('%.3f'%((1 - p) * 100))    