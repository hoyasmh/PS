#include <stdio.h>
int main()
{
	long long n;
	scanf("%lld", &n);
	printf("%s\n", (n % 5 == 2 || n % 5 == 0)? "CY":"SK");
	return 0;
}
