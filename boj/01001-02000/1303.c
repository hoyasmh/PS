#include <stdio.h>
char map[101][101];
int chk[101][101], dx[4] ={-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1}, i, j, n, m, cnt, w, b;
void dfs(int r, int c, char ch)
{
	if (r < 0 || r >= n || c < 0 || c >= m || chk[r][c] || map[r][c] != ch) return;
	chk[r][c] = 1;
	cnt++;
	for (int i = 0; i < 4; i++)
		dfs(r + dx[i], c + dy[i], ch);
}

int main()
{
	scanf("%d%d", &m, &n);
	for (i = 0;i < n; i++)
		scanf("%s", map[i]);
	for (i = 0;i < n; i++)
		for(j = 0; j < m; j++)
			if (!chk[i][j]){
				cnt = 0;
				dfs(i, j, map[i][j]);
				if(map[i][j] == 'W')
					w += cnt * cnt;
				else
					b += cnt * cnt;
			}
	printf("%d %d\n", w, b);
	return 0;
}
