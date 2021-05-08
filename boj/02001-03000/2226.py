n = int(input())
a = 1
for i in range(n - 2):
    a = a * 2 - (i % 2)
print(a - n % 2)    
    