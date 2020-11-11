t=str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ','32123323322122122212111221')
a,b=input(),input()
s=''.join([i+j for i,j in zip(a,b)])
l=[int(i) for i in s.translate(t)]
while len(l)>2:
    l=[(l[i]+l[i+1])%10 for i in range(len(l)-1)]
print(str(l[0])+str(l[1]))


X=input
A=list(map(lambda r:int('32123323322122122212111221'[ord(r)-65]),eval(str(list(zip(X(),X()))).replace('(','').replace(')',''))))
exec("B=[(h + j)%10 for (h, j) in zip(A[:-1], A[1:])];A=B;"*(len(A)-2))
print(''.join(list(map(str,A))))
