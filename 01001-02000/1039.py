#https://www.acmicpc.net/problem/1039
n, k = map(int, input().split())
max = 0
idx = 0
l = list(str(n))
length = len(l)
if(length == 1 or (length == 2 and l[1] == '0')):
    max = -1
def swap(l, cnt, i, j):
    ll = l[:]
    ll[i], ll[j] = ll[j], ll[i]
    global max
    global idx
    if int(''.join(ll)) > max:
        max = int(''.join(ll))
        idx = k - cnt
    if cnt < k:
        for ii in range(i, length-1):
            for j in range(i+1, length):
                if ll[j] > ll[ii]:
                    swap(ll, cnt + 1, ii, j)
if max != -1:
    swap(l, 0, 0, 0)
    if idx % 2 and len(l) == len(set(l)):
        temp = str(max)
        max = int(temp[:-2] + temp[-1] + temp[-2])
print(max)
