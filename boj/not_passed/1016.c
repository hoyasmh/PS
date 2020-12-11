#include <stdio.h>
#include <stdlib.h>
long long find(long long n){
	long long i,j = 0;
	for (i = 2; i * i <= n; i++)
		if (n % (i * i) == 0) return i;
	return n;
}
int main()
{
	long long min, max, i, j, len, temp, cnt = 0;
	char *chk;
	scanf("%lld%lld", &min, &max);
	len = max - min + 1;
	chk = (char*)calloc(len, sizeof(char));
	for (i = 0; i < len; i++){
		if (!chk[i]){
			temp = find(min + i);
			if (temp != min + i){
				chk[i] = 1;
				for (j = i + temp * temp; j < len; j += temp * temp)
					chk[j] = 1;
			}
		}
	}
	while(len--)
		if(!chk[len]) cnt++;
	printf("%lld\n", cnt);
}
