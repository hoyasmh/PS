s=input()
if s[0]=='0' and s[1]=='x':
    print(int(s[2:],16))
elif s[0]=='0':
    print(int(s[1:],8))
else:
    print(s)
