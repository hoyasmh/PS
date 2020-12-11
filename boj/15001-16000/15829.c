#include <stdio.h>

int main()
{
	long long n, ans = 0;
	char c[51];
	
	scanf("%lld%s", &n, c);
	while(n--)
		ans = (ans *31 + c[n] - 96) % 1234567891;
	printf("%lld\n", ans);
	return 0;
}
