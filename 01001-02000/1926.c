#include <stdio.h>
int map[501][501], dr[4] = {-1, 1, 0, 0}, dc[4] = {0, 0, -1, 1}, n, m, i, j, max, cnt, num;
void dfs(int r, int c){
	if (r < 0 || r >= n || c < 0 || c >= m || !map[r][c]) return;
	if(++cnt > max) max = cnt;
	map[r][c] = 0;
	for (int i = 0; i < 4; i++)
		dfs(r + dr[i], c + dc[i]);
}
int main()
{
	scanf("%d%d", &n, &m);
	for (i = 0; i < n; i++)
		for (j = 0; j < m; j++)
			scanf("%d", &map[i][j]);
	for (i = 0; i < n; i++)
		for (j = 0; j < m; j++)
			if (map[i][j] == 1){
				cnt = 0;
				num++;
				dfs(i, j);
			}
	printf("%d\n%d\n", num, max);
	return 0;
}
