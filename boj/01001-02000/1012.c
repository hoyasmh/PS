#include <stdio.h>
int map[51][51], dr[4] = {-1, 1, 0, 0}, dc[4] = {0, 0, -1, 1}, t, q, n, m, i, j, cnt;
void dfs(int r, int c){
	if (r < 0 || r >= n || c < 0 || c >= m || !map[r][c]) return;
	map[r][c] = 0;
	for (int i = 0; i < 4; i++)
		dfs(r + dr[i], c + dc[i]);
}
int main()
{
	int x, y;
	scanf("%d", &t);
	while (t--){
		scanf("%d%d%d", &m, &n, &q);
		cnt = 0;
		for (i = 0; i < q; i++){
			scanf("%d%d", &x, &y);
			map[y][x] = 1;
		}
		for (i = 0; i < n; i++){
			for (j = 0; j < m; j++){
				if (map[i][j]){
					cnt++;
					dfs(i, j);
				}
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}
