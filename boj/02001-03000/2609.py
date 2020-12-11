a, b = map(int, input().split())
c=a*b
while b%a !=0:
    a, b = b%a, a
print('{}\n{}'.format(a,c//a))
