#include <stdio.h>
int main()
{
	int p[250000] = {1, 1,}, n, i = 1, j, cnt;
	while (++i < 500)
		if (p[i] == 0)
			for (j = i * i; j < 246914; j += i)
				p[j] = 1;
	scanf("%d", &n);
	while (n){
		cnt = 0;
		for (i = n + 1; i <= n * 2; i++)
			if (!p[i]) cnt++;
		printf("%d\n", cnt);
		scanf("%d", &n);
	}
	return 0;
}

