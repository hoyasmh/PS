#include <stdio.h>

int main()
{
	long long n, ans = 0;

	scanf("%lld", &n);
	while(--n)
		ans = (ans * 2 + 2) % 1000000007;
	printf("%lld\n", (ans * 4 + 3) % 1000000007);
	return 0;
}
