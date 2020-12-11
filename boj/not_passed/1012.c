// 사이클체크 필요(DP 사용)
#include <stdio.h>
int i, j, n, m, max, map[51][51], chk[51][51], visited[51][51], dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};
void dfs(int x, int y, int cnt)
{
	int temp, i;
	if ((temp = map[x][y]) == 0 || x < 0 || x >= n || y < 0 || y >= m || max == -1) return;
	if (chk[x][y]){
		max = -1;
		return;
	}
	if(visited[x][y]) return;
	if (cnt > max) max = cnt;
	visited[x][y] = cnt; 
	for (i = 0; i < 4; i++)
	{
		chk[x][y] = 1;
		dfs(x + temp * dx[i], y + temp *dy[i], cnt + 1);
		chk[x][y] = 0;
	}
}
int main()
{
	char str[51];
	scanf("%d%d", &n, &m);
	for (i = 0; i < n; i++){
		scanf("%s", str);
		j = -1;
		while (str[++j]){
			if (str[j] == 'H')
				map[i][j] = 0;
			else
				map[i][j] = str[j] - '0';
		}
	}
	dfs(0, 0, 1);
	printf("%d\n", max);
	return 0;
}
