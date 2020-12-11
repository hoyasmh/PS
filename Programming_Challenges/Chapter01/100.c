#include <stdio.h>
int main()
{
	long long lbound, ubound, cnt, max, i, temp;
	int chk[1000001] = {0,};
	while(scanf("%ld%ld", &lbound, &ubound) == 2){
		printf("%ld %ld ", lbound, ubound);
		max = 0;
		if (lbound > ubound){
			temp = lbound;
			lbound = ubound;
			ubound = temp;
		}
		for (i = lbound; i <= ubound; i++){
			cnt = 0;
			temp = i;
			if (!chk[i]){
				while (temp > 1000000 || !chk[temp] && temp > 1){
					if (temp % 2 == 0) 
						temp /= 2;
					else
						temp = temp * 3 + 1;
					cnt++;
				}
				chk[i] = chk[temp] + cnt;
			}
			max = chk[i] > max ? chk[i] : max;
		}
		printf("%ld\n", max + 1);
	}
	return 0;
}
