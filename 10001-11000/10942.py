input()
s=input()[::2]
for i in [0]*int(input()):
    a,b=map(int, input().split())
    if s[a-1:b]==s[a-1:b][::-1]:
        print(1)
    else:
        print(0)
