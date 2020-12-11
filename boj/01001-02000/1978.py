n=int(input())
p=list(map(int, input().split()))
count=0
for i in p:
    if i >= 2:
        for j in range(2, int(i**0.5)+2):
            if i%j==0 and i != j:
                break
            elif j==int(i**0.5)+1 or i==j:
                count+=1
print(count)
