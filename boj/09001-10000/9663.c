#include <stdio.h>

int row[15];
int rdiag[29];
int ldiag[29];
int cnt;

void dfs(int m, int n)
{
	int i;
	for (i = 0; i < n; i++)
	{
		if (!row[i] && !rdiag[m + i] && !ldiag[m - i + n - 1])
		{
			if (m + 1 == n)
				cnt++;
			else
			{
				row[i] = 1;
				rdiag[m + i] = 1;
				ldiag[m - i + n - 1] = 1;
				dfs(m + 1, n);
				row[i] = 0;
				rdiag[m + i] = 0;
				ldiag[m - i + n - 1] = 0;
			}
		}
	}
}

int main()
{
	int n;
	scanf("%d", &n);
	dfs(0, n);
	printf("%d\n", cnt);
	return 0;
}
