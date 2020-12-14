#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int ram[1001], reg[11], i, n, mode, dst, src, cnt, flag;
	char cmd[10], first;
	scanf("%d\n", &n);
	while(n--){
		memset(reg, 0, sizeof(reg));
		memset(ram, 0, sizeof(ram));
		cnt = 0;
		for (i = 0; (first = getchar()) != '\n' && !feof(stdin); i++){
			scanf("%d", &ram[i]);
			ram[i] += (first - '0') * 100;
			getchar();
		}
		flag = 1;
		i = 0;
		while (flag){
			mode = ram[i] / 100;
			dst = ram[i] / 10 % 10;
			src = ram[i] % 10;
			cnt++;
			i++;
			switch (mode){
				case 1:
					flag = 0;
					break;
				case 2:
					reg[dst] = src;
					break;
				case 3:
					reg[dst] = (reg[dst] + src) % 1000;
					break;
				case 4:
					reg[dst] = (reg[dst] * src) % 1000;
					break;
				case 5:
					reg[dst] = reg[src];
					break;
				case 6:
					reg[dst] = (reg[dst] + reg[src]) % 1000;
					break;
				case 7:
					reg[dst] = (reg[dst] * reg[src]) % 1000;
					break;
				case 8:
					reg[dst] = ram[reg[src]];
					break;
				case 9:
					ram[reg[src]] = reg[dst];
					break;
				case 0:
					if(reg[src])
						i = reg[dst];
					break;
			}
		}
		printf("%d\n", cnt);
		if (n) printf("\n");
	}
	return 0;
}
