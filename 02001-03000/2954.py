s=input()
t=''
j=0
while j<len(s):
    t=t+s[j]
    if s[j] in 'aeiou':
        j=j+3
    else:
        j=j+1
print(t)
