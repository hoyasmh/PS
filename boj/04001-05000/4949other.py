s=input()
while s!='.':
    l=[0]
    for i in s:
        if i in '[(':
            l.append(i)
        if i==']':
            if l[-1]=='[':
                l.pop()
            else:
                print('no')
                break
        if i==')':
            if l[-1]=='(':
                l.pop()
            else:
                print('no')
                break
    else:
        print(['no','yes'][len(l)==1])
    s=input()

import re
while id:
 id=s=input()[:-1]
 while 1:
  S=re.sub(r'[^[\]()]|\[\]|\(\)','', s)
  if S==s:break
  s=S
 id>''!=print('yneos'[s>''::2])

 while 1:
    s,x,r=input(),[],1
    if s==".":break
    for c in s:
        if c in["[","("]:x.append(c)
        elif c=="]"and(len(x)<1 or x.pop()!="[")or c==")"and(len(x)<1 or x.pop()!="("):r=0;break
    if len(x):r=0
    print(r and"yes"or"no")    
