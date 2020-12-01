#include <stdio.h>
char map[251][251];
int n, m , i, j, v, k, tot_v, tot_k, dr[4] = {-1, 1, 0, 0}, dc[4] = {0, 0, -1, 1};
void dfs(int r, int c){
	if (r < 0 || r >= n || c < 0 || c >= m || map[r][c] == 'x' || map[r][c] == '#') return;
	if (map[r][c] == 'v') v++;
	else if (map[r][c] == 'k') k++;
	map[r][c] = 'x';
	for (int i = 0; i < 4; i++)
		dfs(r + dr[i], c + dc[i]);
}
int main()
{
	scanf("%d%d", &n, &m);
	for (i = 0; i < n; i++)
		scanf("%s", map[i]);
	for (i = 0; i < n; i++){
		for (j = 0; j < m; j++){
			if (map[i][j] == '.' || map[i][j] == 'v' || map[i][j] == 'k'){
				v = 0;
				k = 0;
				dfs(i, j);
				k > v? (tot_k += k) : (tot_v += v);
			}
		}
	}
	printf("%d %d\n", tot_k, tot_v);
	return 0;
}

