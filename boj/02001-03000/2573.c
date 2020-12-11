#include <stdio.h>
#define max(a, b) (a > b? a : b)
int map[301][301], chk[301][301], dr[4] = {-1, 1, 0, 0}, dc[4] = {0, 0, -1, 1}, n, m, i, j, cnt, time;
void dfs(int r, int c)
{
	int temp = 0;
	if (r < 0 || r >= n || c < 0 || c >= m || !map[r][c] || chk[r][c] != -1) return;
	for (int i = 0; i < 4; i++)
		if (map[r + dr[i]][c + dc[i]] == 0)
			++temp;
	chk[r][c] = temp;
	for (int i = 0; i < 4; i++)
		dfs(r + dr[i], c + dc[i]);
}
int main()
{
	int flag = 1, flag2 = 1;
	scanf("%d%d", &n, &m);
	for (i = 0; i < n; i++)
		for (j = 0; j < m; j++)
			scanf("%d", &map[i][j]);
	while(flag){
		cnt = 0;
		for (i = 0; i < n; i++)
			for (j = 0; j < m; j++){
				map[i][j] = max(0, map[i][j] - chk[i][j]);
				if (map[i][j]){
					flag2 = 0;
					chk[i][j] = -1;
				}
			}
		if (flag2 == 1){
			time = 0;
			break;
		}
		flag2 = 1;
		for (i = 1; i < n-1; i++)
			for (j = 1; j < m-1; j++)
				if (map[i][j] && chk[i][j] == -1){
					cnt++;
					if(cnt > 1) flag = 0;
					dfs(i, j);
				}
		time++;
	}
	printf("%d\n", !time? 0 : time -1);
	return 0;
}
