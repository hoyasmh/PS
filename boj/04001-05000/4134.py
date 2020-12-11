def solution(n):
    if n==2:
        return 1
    prime=[1]*((n-1)//2)
    for i in range(int(n**.5)):
        if prime[i]==1:
            temp=2*(i**2)+6*i+3
            while((n-1)//2-temp>0):
                prime[temp]=0
                temp+=2*i+3
    return [1]+prime

n=86028121
# m=int(''.join([str(i) for i in solution(n)]),2)
print(sum(solution(n)))
