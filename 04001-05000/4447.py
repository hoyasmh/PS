for i in range(int(input())):
    s=input()
    l=[s.upper().count(chr(j)) for j in (66,71)]
    print(s,'is',[['GOOD','A BADDY'][l[0]>l[1]],'NEUTRAL'][l[0]==l[1]])
