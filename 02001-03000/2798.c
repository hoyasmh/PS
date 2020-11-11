#include <stdio.h>

int main()
{
	int i, j, k, n, m, max = 0, temp, arr[101];
	scanf("%d%d", &n, &m);
	for (i = 0;i < n;i++)
		scanf("%d", arr + i);
	for (i = 0; i < n-2;i++)
		for(j = i + 1;j < n - 1;j++)
			for(k = j + 1;k < n;k++)
			{
				temp = arr[i] + arr[j] + arr[k];
				if ( temp > max && temp <=m)
					max = temp;
			}
	printf("%d\n", max);
	return 0;
}
				


