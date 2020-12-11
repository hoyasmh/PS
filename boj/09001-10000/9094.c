#include <stdio.h>
int main()
{
	int t, n, m, i, j, k, cnt;
	scanf("%d", &t);
	for (i = 0; i < t; i++){
		scanf("%d%d", &n, &m);
		cnt = 0;
		for (j = 1; j < n-1; j++)
			for (k = j + 1; k < n; k++)
				if ((j * j + k * k + m) % (j * k) == 0)
					cnt++;
		printf("%d\n", cnt);
	}
	return 0;
}

