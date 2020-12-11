import collections
import math
n,k=map(int,input().split())
l=collections.Counter([input() for i in range(n)]).values()
print(sum([math.ceil(j/k) for j in l]))
