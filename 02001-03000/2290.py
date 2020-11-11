def f(n,r,s):
    if r==0:
        return ' '+'-'*s+' ' if n in '23567890' else ' '*(s+2)
    elif r==1 and n in '1237':
        return ' '*(s+1)+'|'
    elif r==1 and n in '56':
        return '|'+' '*(s+1)
    elif r==1 and n in '4890':
        return '|'+' '*s+'|'
    elif r==2 and n in '2345689':
        return '-'*s
    elif r==3 and n in '134579':
        return ' '*(s+1)+'|'
    elif r==3 and n in '2':
        return '|'+' '*(s+1)
    elif r==3 and n in '680':
        return '|'+' '*s+'|'
    elif r==4 and n in '2356890':
        return '-'*s
