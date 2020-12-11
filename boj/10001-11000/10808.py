import string
a=list(string.ascii_lowercase)
c=[0]*26
s=input()
for i in s:
    c[a.index(i)]+=1
print(*c)
