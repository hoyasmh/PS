s=input()
while s!='#':
    print(' '.join([i[::-1] for i in s.split()]))
    s=input()
