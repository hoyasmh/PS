#include <stdio.h>
int main()
{
	long long n;
	scanf("%lld", &n);
	printf("%s\n", (n % 2)? "SK":"CY");
	return 0;
}
