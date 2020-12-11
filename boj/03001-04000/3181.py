l=['i','pa','te','ni','niti','a','ali','nego','no','ili']
s=input().split()
for i in range(len(s)):
    if i==0 or s[i] not in l:
        print(s[i][0].upper(),end='')
