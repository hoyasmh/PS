s=input()
while s!='#':
    print(s[:-1]+'10'['eo'[s.count('1')%2]==s[-1]])
    s=input()
