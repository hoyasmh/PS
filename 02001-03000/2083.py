s=input().split()
while s[0]!='#':
    print(s[0],['Junior','Senior'][int(s[1])>17 or int(s[2])>79])
    s=input().split()
