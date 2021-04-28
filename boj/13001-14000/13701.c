#include <stdio.h>

int n,arr[1<<20];
int main()
{
	while(~scanf("%d", &n))
	{
		if(!(arr[n/32]&1<<(n%32)))
		{
			arr[n/32] |= 1<<(n%32);
			printf("%d ",n);
		}
	}
	return 0;
}
