#include <stdio.h>

int main()
{   
    int     n, m, i, j, i2, j2, field_id = 1;
    char    map[102][102], str[102];
    scanf("%d%d", &n, &m);
    while (n || m){
        for (i =1; i <= n; i++)
            for (j = 1; j <= m; j++)
				map[i][j] = '0';
        for (i = 1; i <= n; i++){
			scanf("%s", str);
            for (j = 1; j <= m; j++){
                if (str[j - 1] == '*'){
                    map[i][j] = '*';
                    for (i2 = -1; i2 < 2; i2++){
						for (j2 = -1; j2 < 2; j2++){
							if (map[i + i2][j + j2] != '*')
								map[i + i2][j + j2]++;
						}
					}
                }
            }
        }
		if (field_id > 1)
			printf("\n");
        printf("Field #%d:\n", field_id++);
        for (i = 1; i <= n; i++){
            for (j = 1; j <= m; j++){
                printf("%c",map[i][j]);
            }
            printf("\n");
        }
        scanf("%d%d", &n, &m);
    }
    return 0;
}

