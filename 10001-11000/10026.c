#include <stdio.h>
char map[2][101][101], str[101];
int dr[4] = {-1, 1, 0, 0}, dc[4] = {0, 0, -1, 1}, n, i, j, k, cnt[2];
void dfs(int r, int c, int mode, char color){
	if (r < 0 || r >= n || c < 0 || c >= n ||map[mode][r][c] == 'x' || map[mode][r][c] != color) return;
	map[mode][r][c] = 'x';
	for (int i = 0; i < 4; i++)
		dfs(r + dr[i], c + dc[i], mode, color);
}
int main()
{
	scanf("%d", &n);
	for (i = 0; i < n; i++){
		scanf("%s", str);
		for (j = 0; j < n; j++){
			map[0][i][j] = str[j];
			map[1][i][j] = (str[j] == 'R'? 'G':str[j]);
		}
	}
	for (i = 0; i < n; i++){
		for(j = 0; j < n; j++){
			for (k = 0; k < 2; k++){
				if(map[k][i][j] != 'x'){
					cnt[k]++;
					dfs(i, j, k, map[k][i][j]);
				}
			}
		}
	}
	printf("%d %d\n", cnt[0], cnt[1]);
	return 0;
}
