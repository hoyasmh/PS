#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int ch, k, len;
char max[8];
void swap(char *a, char *b){
	char temp = *a;
	*a = *b;
	*b = temp;
}
int dup(char *num, int len){
	int chk[10] = {0,};
	while (len--){
		if (chk[num[len] - '0'])
			return 0;
		chk[num[len] - '0'] = 1;
	}
	return 1;
}
void dfs(char *num, int cnt, int begin){
	if (atoi(num) > atoi(max)){
		strcpy(max, num);
		ch = k - cnt;
	}
	if (cnt < k){
		for (int i = begin + 1; i < len; i++){
			if (num[i] > num[begin]){
				swap(&num[i], &num[begin]);
				dfs(num, cnt + 1, begin + 1);
				swap(&num[i], &num[begin]);
			}
			else
				dfs(num, cnt, i + 1);
		}
	}
}
int main()
{
	char n[8];
	scanf("%s%d", &n, &k);
	len = strlen(n);
	if (len == 1 || len == 2 && n[1] == '0'){
		printf("%d\n", -1);
		return 0;
	}
	dfs(n, 0, 0);
	if (ch % 2 && dup(n, len))
		swap(&max[len - 1], &max[len - 2]);
	printf("%d\n", atoi(max));
	return 0;
}
