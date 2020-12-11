s=input()
while s!='#':
    n=len(s)
    for i in range(n):
        if s[i] in 'aeiou':
            print(s[i:]+s[:i]+'ay')
            break
    else:
        print(s+'ay')        
    s=input()
