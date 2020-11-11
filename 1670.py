n=100
l=[1]
for i in range(n//2):
    l.append(sum([l[k]*l[i-k] for k in range(i+1)])%987654321)
print(l)
