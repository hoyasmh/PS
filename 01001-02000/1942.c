#include <stdio.h>
int chk[26], dr[4] = {-1, 1, 0, 0}, dc[4] = {0, 0, -1, 1}, n, m, i, j, max;
char map[21][21];
void dfs(int r, int c, int cnt){
	if (r < 0 || r >= n || c < 0 || c >= m || chk[map[r][c] - 'A']) return;
	if (cnt > max) max = cnt;
	for (int i = 0; i < 4; i++){
		chk[map[r][c] - 'A'] = 1;
		dfs(r + dr[i], c + dc[i], cnt + 1);
		chk[map[r][c] - 'A'] = 0;
	}
}
int main()
{
	int cnt = 0;
	scanf("%d%d", &n, &m);
	for (i = 0; i < n; i++)
		scanf("%s", map[i]);
	dfs(0, 0, 1);
	printf("%d\n", max);
	return 0;
}

