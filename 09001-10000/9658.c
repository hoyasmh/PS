#include <stdio.h>
int main()
{
	int n;
	scanf("%d", &n);
	printf("%s\n", (n % 7 == 1 || n % 7 == 3)? "CY":"SK");
	return 0;
}
