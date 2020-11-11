s=input().strip()
print(s.count(' ')-s.count('-')-s.count(' 0')+1-bool(s[0]=='0'))
