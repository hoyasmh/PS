import sys
l=[1,2,6,24,120]
s=input()[::-1]
while s!='0':
    print(sum([l[i]*int(s[i]) for i in range(len(s))]))
    s=sys.stdin.readline().strip()[::-1]
