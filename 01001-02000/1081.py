# def f(n,k):
#     return 5*k*10**(n-2)*(9*n+k-10)+k
# def s(m):
#     s=0
#     for i in range(len(m)):
#         s+=f(len(m)-i,int(m[i]))+
#     return s
#a,b=input().split()
#print(s(b)-s(a)+sum([int(j) for j in a]))
# print(s('12'))
# n=407
# m=len(str(n))-1
# k=int(str(n)[0])
# s=0
# print(m,k)
# for i in range(n+1):
#     s+=sum([int(j) for j in str(i)])
# print(s)

# print(45*k*m*(10**(m-1))+k*(k-1)*(10**m)//2)
a,b=input().split()
def r(m,k):
    return 45*k*m*(10**(m-1))+k*(k-1)*(10**m)//2
def q(p):
    l=[int(i) for i in p]
    a=0
    for i in range(len(p)-1):
        a+=sum(l[:i+1])*l[i+1]*10**(len(p)-2-i)
    for j in range(len(p)):
        a+=r(len(p)-1-j,l[j])+l[j]
    return int(a)
print(q(b)-q(a)+sum([int(k) for k in a]))
