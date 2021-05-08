import heapq
import sys
l = []
n = int(sys.stdin.readline())
for i in range(n):
    cmd = int(sys.stdin.readline())
    if cmd == 0:
        print(0 if len(l) == 0 else heapq.heappop(l))
    else:
        heapq.heappush(l, cmd)