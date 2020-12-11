m=['Not a pangram','Pangram!','Double pangram!!','Triple pangram!!!']
for i in range(int(input())):
    l=[0]*26
    s=input().upper()
    for j in s:
        if j.isalpha():
            l[ord(j)-65]+=1
    print('Case {}: {}'.format(i+1,m[min(l)]))
