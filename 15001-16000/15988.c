#include <stdio.h>
int main()
{
	unsigned int arr[1000001] = {1, 2, 4,}, t, n, i = 3;
	scanf("%u", &t);
	while (t--){
		scanf("%u", &n);
		if (arr[n]) printf("%u\n", arr[n - 1]);
		else{
			while (i <= n){
				arr[i] = (arr[i - 1] + arr[i - 2] + arr[i - 3]) % 1000000009;
				i++;
			}
			printf("%u\n", arr[n - 1]);
		}
	}
	return 0;
}

