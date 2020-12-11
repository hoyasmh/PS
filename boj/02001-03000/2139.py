m=[0,31,28,31,30,31,30,31,31,30,31,30,31]
a,b,c=map(int,input().split())
while a!=0:
    print(sum(m[:b])+a+sum([c%4==0,c%100==0,c%400==0])%2 if b>2 else sum(m[:b])+a)
    a,b,c=map(int,input().split())
