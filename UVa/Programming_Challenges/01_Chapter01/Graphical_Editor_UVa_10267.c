#include <stdio.h>

#define MAX 250
#define swap(a, b) temp = a; a = b; b = temp;

char map[MAX + 2][MAX +2];
int m, n, d[2] = {-1, 1}, chk[MAX + 2][MAX + 2];

void dfs(int i, int j, char og_color, char ch_color){
	int idx;
	if (i < 1 || i > n || j < 1 || j > m || chk[i][j] || map[i][j] != og_color) return;
	map[i][j] = ch_color;
	chk[i][j] = 1;
	for (idx = 0; idx < 4; idx++){
		dfs(i +d[idx % 2] * ((idx / 2) ^ 1), j + d[idx % 2] * (idx / 2), og_color, ch_color);
	}
}

int main()
{
	char mode = '\0', color, name[100];
	int i, j, x1, x2, y1, y2, temp;
	while(mode != 'X'){
		scanf("%c", &mode);
		switch (mode){
			case 'I':
				scanf("%d %d", &m, &n);
			case 'C':
				for (i = 1; i <= n; i++)
					for (j = 1; j <= m; j++)
						map[i][j] = 'O';
				break;
			case 'L':
				scanf("%d %d %c", &x1, &y1, &color);
				map[y1][x1] = color;
				break;
			case 'V':
				scanf("%d %d %d %c", &x1, &y1, &y2, &color);
				if (y1 > y2){
					swap(y1, y2)
				}
				for (i = y1; i <= y2; i++)
					map[i][x1] = color;
				break;
			case 'H':
				scanf("%d %d %d %c", &x1, &x2, &y1, &color);
				if (x1 > x2){
					swap(x1, x2)
				}
				for (i = x1; i <= x2; i++)
					map[y1][i] = color;
				break;
			case 'K':
				scanf("%d %d %d %d %c", &x1, &y1, &x2, &y2, &color);
				for (i = y1; i <= y2; i++)
					for (j = x1; j <= x2; j++)
						map[i][j] = color;
				break;
			case 'F':
				for (i = 1; i <= n; i++)
					for (j = 1; j <= m; j++)
						chk[i][j] = 0;
				scanf("%d %d %c", &x1, &y1, &color);
				dfs(y1, x1, map[y1][x1], color);
				break;
			case 'S':
				scanf("%s", name);
				printf("%s\n", name);
				for (i = 1; i <= n; i++){
					for (j = 1; j <= m; j++){
						printf("%c", map[i][j]);
					}
					printf("\n");
				}
				break;
		}
	}
	return 0;
}
