#include <stdio.h>
int map[101][101], dr[4] = {-1, 1, 0, 0}, dc[4] = {0, 0, -1, 1}, n, m, k, i, j, max, size;
void dfs(int r, int c){
	if (r < 0 || r >= n || c < 0 || c >= m || !map[r][c]) return;
	map[r][c] = 0;
	if(++size > max) max=size;
	for (int i = 0; i < 4; i++)
		dfs(r + dr[i], c + dc[i]);
}
int main()
{
	int x, y;
	scanf("%d%d%d", &n, &m, &k);
	for (i = 0; i < k; i++){
		scanf("%d%d", &x, &y);
		map[x-1][y-1] = 1;
	}
	for (i = 0; i < n; i++){
		for (j = 0; j < m ; j++){
			if (map[i][j]){
				size = 0;
				dfs(i, j);
			}
		}
	}
	printf("%d\n", max);
}
		
