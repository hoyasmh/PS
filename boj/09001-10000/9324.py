for j in range(int(input())):
    s=input()
    l=[0]*26
    for i in range(len(s)):
        l[ord(s[i])-65]+=1
        if l[ord(s[i])-65]%4==3 and (i==len(s)-1 or s[i]!=s[i+1]):
            print('FAKE')
            break
        elif i==len(s)-1:
            print('OK')
