#include <stdio.h>
int map[101][101], chk[101][101], dr[4] = {-1, 1, 0, 0}, dc[4] = {0, 0, -1, 1}, n, i, j, height, max, cnt;
void dfs(int r, int c){
	if (r < 0 || r >= n || c < 0 || c >= n || chk[r][c] || map[r][c] <= height) return;
	chk[r][c] = 1;
	for (int i = 0; i < 4; i++)
		dfs(r + dr[i], c + dc[i]);
}
void init(int (*arr)[101], int n){
	int i, j;
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
			arr[i][j] = 0;
}
int main()
{
	scanf("%d", &n);
	for (i = 0; i < n; i++){
		for (j = 0; j < n; j++){
			scanf("%d", &map[i][j]);
			if (map[i][j] > height) height = map[i][j];
		}
	}
	while(height--){
		init(chk, n);
		cnt = 0;
		for (i = 0; i < n; i++){
			for (j = 0; j < n; j++){
				if (map[i][j] > height && !chk[i][j]){
					if(++cnt > max) max=cnt;
					dfs(i, j);
				}
			}
		}
	}
	printf("%d\n", max);
}
		
