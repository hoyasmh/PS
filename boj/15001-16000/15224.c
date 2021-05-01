#include <stdio.h>

int mod = 1e+9 + 7, cnt;
int odd(long long n)
{
	for(cnt = 0;n>1; cnt++)
		n = n & 1 ? n+1:n/2;
	return cnt;
}
int evenodd(long long n)
{
	if (n <= 1)
		return 0;
	if (n == 2)
		return 1;
	if (n % 2 == 0)
		return (evenodd(n/2)*2+n/2*3-2)%mod;
	return (evenodd(n-1)+odd(n))%mod;
}

int main()
{
	long long l, r;
	scanf("%lld%lld", &l, &r);
	printf("%d\n", (mod+evenodd(r)-evenodd(l-1))%mod);
}




