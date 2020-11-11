for i in range(int(input())):
    n=int(input())
    s=input()
    print('Data Set {}:\n{}\n'.format(i+1,n+s.count('c')-s.count('b')))
