#include <stdio.h>
int main()
{
	int n;
	scanf("%d", &n);
	printf("%s\n", (n % 7 == 2 || n % 7 == 0)? "CY":"SK");
	return 0;
}
