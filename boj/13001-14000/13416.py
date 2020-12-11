for i in range(int(input())):
    m=0
    for j in range(int(input())):
        m+=max(list(map(int,input().split()))+[0])
    print(m)
