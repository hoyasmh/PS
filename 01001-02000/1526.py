n=int(input())
for i in range(2,131):
    m=int(''.join(['47'[int(j)] for j in bin(131-i)[3:]]))
    if m<=n:
        print(m)
        break
