#include <stdio.h>

int main()
{
	int costs[1001], n, i, sum, ave, ans, re;
	double cost;
	scanf("%d", &n);
	while(n){
		sum = 0;
		for (i = 0; i < n; i++){
			scanf("%lf", &cost);
			costs[i] = (int)(cost * 100 + 0.5);
			sum += costs[i];
		}
		ave = sum / n;
		re = sum % n;
		ans = 0;
		for (i = 0; i < n; i++){
			if (costs[i] > ave){
				ans += costs[i] - ave;
				if (re-- > 0) ans--;
			}
		}
		printf("$%.2f\n", ans / 100.0);
		scanf("%d", &n);
	}
	return 0;
}


