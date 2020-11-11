input()
print(sum([len(i)*(len(i)+1)//2 for i in input()[::2].split('0')]))
