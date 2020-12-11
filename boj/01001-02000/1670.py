l=[1]
for i in range(int(input())//2):
    l.append(sum([l[j]*l[i-j] for j in range(i+1)])%987654321)
print(l[-1]%987654321)
