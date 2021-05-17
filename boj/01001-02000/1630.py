n = int(input()) + 1
l = [i for i in range(n)]
ans = 1
for i in range(n):
    if l[i] > 1 and ans:
        ans = ans * l[i] % 987654321
        for j in range(i * 2, n, i):
            l[j] //= l[i]
print(ans)            
    