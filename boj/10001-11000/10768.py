n=(int(input())-1)*31+int(input())
print("Special"  if n==49 else ["Before","After"][bool(n//49)])
