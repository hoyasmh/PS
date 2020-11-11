n=int(input())
for i in range(n):
    p,m,f,c=map(int, input().split())
    print((m//p*c-c)//(f-c)-m//p*c//f)
