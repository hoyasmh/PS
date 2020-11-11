for i in range(int(input())):
    a,b=input().split()
    print(int(str(int(a[::-1])+int(b[::-1]))[::-1]))

exec('print(int(str(sum(int(x[::-1]) for x in input().split()))[::-1]));'*int(input()))
