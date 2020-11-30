#include <stdio.h>

int ans;

int find(int n, int m)
{
	int i;

	if (m / n == 0)
		find(n / 10, m);
	else
	{
		i = 1;
		while(m)
		{
			ans = ans * 10 + m / n;
			m %= n;
			n = n / 10 - i;
			i *= 10;
			if(n <= 0)
				return 0;
		}
	}
}

int main()
{
	int n;

	scanf("%d", &n);
/*	if (n % 9 != 0)
	{
		printf("%d\n", -1);
		return 0;
	}*/
	if(!find(111111, n/9))
	{
		printf("%d\n", -1);
		return 0;
	}
	printf("%d\n", ans);
	return 0;
}
