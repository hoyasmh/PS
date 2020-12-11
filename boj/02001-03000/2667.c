#include <stdio.h>
#include <stdlib.h>
int arr[325], dr[4] = {-1, 1, 0, 0}, dc[4] = {0, 0, -1, 1}, n, i, j, cnt, num;
char map[26][26];
void dfs(int r, int c){
	if (r < 0 || r >=n || c < 0 || c >= n || map[r][c] == '0') return;
	map[r][c] = '0';
	cnt++;
	for (int i = 0; i < 4; i++)
		dfs(r + dr[i], c + dc[i]);
}
int cmp(const void *a, const void *b)
{
	return (*(int*)a > *(int*)b);
}
int main()
{
	scanf("%d", &n);
	for (i = 0; i < n; i++)
		scanf("%s", map[i]);
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++){
			if (map[i][j] == '1'){
				cnt = 0;
				dfs(i, j);
				arr[num++] = cnt;
			}
		}
	qsort(arr, num, sizeof(int), cmp);
	printf("%d\n", num);
	for (i = 0; i < num; i++)
		printf("%d\n", arr[i]);
	return 0;
}
	


