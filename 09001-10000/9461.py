def tri(n):
    if n<=3:
        return 1
    elif n<=5:
        return 2
    else:
        return tri(n-1)+tri(n-5)
print(tri(int(input())))                
