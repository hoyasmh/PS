i=1
while 1:
    s=input()
    if s=='0':
        exit()
    else:
        r,w,l=map(int,s.split())
        print('Pizza {} {} on the table.'.format(i,['does not fit','fits'][4*r*r>=w*w+l*l]))
        i+=1
