for i in range(int(input())):
    s=input()
    s=s*(len(s)%2+1)
    print(*[s[::2],s[1::2]],sep='\n')
