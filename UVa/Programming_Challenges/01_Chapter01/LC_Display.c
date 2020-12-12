#include <stdio.h>
#include <string.h>

int main()
{
	int digit[10][8] = {{0,1,2,4,5,6,-1}, {2, 5,-1}, {0,2,3,4,6,-1}, {0,2,3,5,6,-1},{1,2,3,5,-1},{0,1,3,5,6,-1}, {0,1,3,4,5,6,-1}, {0,2,5,-1}, {0,1,2,3,4,5,6,-1}, {0,1,2,3,5,6,-1}};
	char panel[24][150];
	int s, i, j;
	char n[9];
	scanf("%d%s", &s, n);
	while(s || strcmp(n, "0")){
		int idx = 0;
		int shift = 0;
		for (i = 0; i < 24 ; i++)
			for (j = 0 ; j < 150; j++)
				panel[i][j] = ' ';
		while(n[idx]){
			int *temp = digit[n[idx++] - '0'];
			while (*temp != -1){
				for (i = 0; i < 2 * s + 3; i++){
					for (j = 0; j < s + 2; j++){
						int bias =(s + 1) * (*temp / 3);
						if (*temp % 3 == 0){
							if (i % (s + 1) == 0 && i / (s + 1) == *temp / 3 && j > 0 && j <= s)
								panel[i][j + shift] = '-';
						}
						else if (*temp % 3 == 1){
							if (j == 0 && i > 0 + bias && i <= s + bias)
								panel[i][j + shift] = '|';
						}
						else{
							if (j == s + 1 && i > 0 + bias && i <= s + bias)
								panel[i][j + shift] = '|';
						}
					}
				}
				temp++;
			}
			shift += s + 3;
		}
		for (i = 0; i < 2 * s + 3; i++){
			for (j = 0; j < (s + 3) * strlen(n) -1; j++){
				printf("%c", panel[i][j]);
			}
			printf("\n");
		}
		printf("\n");
		scanf("%d%s", &s, n);
	}
	return 0;
}




