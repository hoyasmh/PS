a, b = map(int, input().split())
l=[i for i in range(1,a+1)]
s=[]
while l:
    c=(b-1)%len(l)
    s.append(str(l.pop(c)))
    l=l[c:]+l[:c]
print('<'+', '.join(s)+'>')
