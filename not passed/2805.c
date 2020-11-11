#include <stdio.h>

int main()
{
	int i, n, m, arr[1000000], l, r, mid, sum, temp;
	scanf("%d%d", &n, &m);
	for (i = 0; i < n; i++)
		scanf("%d", arr + i);
	l = 0;
	r = 2000000000;
	while(l <= r)
	{
		sum = 0;
		mid = (l + r) / 2;
		for(i = 0; i < n; i++)
		{
			if(arr[i] > mid)
				sum += arr[i] - mid;
		}
		if (sum == m)
		{
			printf("%d\n", mid);
			return 0;
		}
		if (sum > m)
		{
			temp = mid;
			l = mid +1;
        }
		else
			r = mid -1;
	}
	printf("%d\n", temp);
	return 0;
}	
