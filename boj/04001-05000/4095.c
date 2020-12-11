#include <stdio.h>
int map[1002][1002], i, j, n, m, max;
int	minimum(int i, int j){
	int min;
	min = (map[i - 1][j] > map[i][j - 1] ? map[i][j - 1] : map[i - 1][j]);
	min = (min > map[i - 1][j - 1] ? map[i - 1][j - 1] : min);
	return (min);
}
int main()
{
	scanf("%d%d", &n, &m);
	while (n && m){
		max = 0;
		for (i = 1; i <= n; i++)
			for (j = 1; j <= m; j++)
				scanf("%d", &map[i][j]);
		for (i = 1; i <= n; i++){
			for (j = 1; j <= m; j++){
				if (map[i][j]){
					map[i][j] = minimum(i, j) + 1;
					if (map[i][j] > max) max = map[i][j];
				}
			}
		}
		printf("%d\n", max);
		scanf("%d%d", &n, &m);
	}
	return 0;
}



