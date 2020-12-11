from collections import Counter as c
l=[int(input()) for i in [0]*10]
print(sum(l)//10,c(l).most_common(1)[0][0], sep='\n')
