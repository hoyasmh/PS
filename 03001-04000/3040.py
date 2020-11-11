import itertools
print(*[j for j in itertools.combinations([int(input()) for i in range(9)],7) if sum(j)==100][0],sep='\n')
