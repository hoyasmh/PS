m, M = map(int, input().split())
length = M - m + 1
l = [1] * length
i = 2
while i * i <= M:
    t = i * i
    for j in range(length):     
        if (m + j) % (i * i) == 0:
            l[j] = 0
            for k in range(j + 1, length, i * i):
                l[k] = 0
            break 
    i += 1        
print(sum(l))            
            
            
