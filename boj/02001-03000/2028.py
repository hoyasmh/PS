for i in range(int(input())):
    n=input()
    print(['NO','YES'][str(int(n)**2)[-len(n):]==n])
