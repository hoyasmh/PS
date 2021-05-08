import heapq as h
n = int(input())
l = [n]
while 1:
    flag = 1
    num = h.heappop(l)
    for j in str(n):
        if j == '0' or j == '1':
            continue
        if num % int(j):
            flag = 0
            break
    if flag:
        print(num)
        break
    for k in range(10):
        h.heappush(l, int(str(num) + str(k)))

    