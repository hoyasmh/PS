m,n=map(int,input().split())
h={input() for i in [0]*m}
s={input() for i in [0]*n}
print(len(h&s),*sorted(list(h&s)),sep='\n')
