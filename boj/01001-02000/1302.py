from collections import Counter
n=int(input())
print((Counter(sorted([input() for i in range(n)])).most_common(1))[0][0])
