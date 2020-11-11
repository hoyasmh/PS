n,m,s=int(input()),int(input()),input()
i,a,c=1,0,0
while i<m:
    if s[i-1]=='I' and s[i:i+2]=='OI':
        i+=2
        a+=1
    else:
        i+=1
        c+=max(0,a-n+1)
        a=0
else:
    c+=max(0,a-n+1)
print(c)


import re
n = int(input())
input()
print(sum(max((len(i)-1)//2-n+1, 0) for i in re.findall('I(?:OI)+', input())))
