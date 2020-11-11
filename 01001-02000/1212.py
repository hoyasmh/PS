print(int(''.join([bin(j)[2:].zfill(3) for j in map(int, '1234')])))
print(bin(int('1234',8))[2:])
