m = int(input())
l = [1] * (m // 2)
p =[2]
for i in range(len(l)):
    if l[i]:
        n = i * 2 + 3
        p.append(n)
        for j in range(i + n, len(l), n):
            l[j] = 0
cnt = 0
for i in range(len(p)):
    total = p[i]
    j = i + 1
    while total < m and j < len(p):
        total += p[j]
        j += 1  
    if total == m:
        cnt += 1
print(cnt)           