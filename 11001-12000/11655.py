s=list(input())
for i in range(len(s)):
    if 65<=ord(s[i])<=90:
        n=ord(s[i])+13
        s[i]=chr(n%91+n//91*65)
    elif 97<=ord(s[i])<=122:
        n=ord(s[i])+13
        s[i]=chr(n%123+n//123*97)   
print(''.join(s))
