l={'AA':'A','AC':'A','AG':'C','AT':'G','CC':'C','CG':'T','CT':'G','GG':'G','GT':'A','TT':'T'}
n=int(input())
s=list(input())
for i in range(n-1):
    s[-2:]=l[''.join(sorted(s[-2:]))]
print(*s)
