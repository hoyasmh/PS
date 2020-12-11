#include <stdio.h>

int map[10001][10002];

int main()
{
	int i=10000, j=10001,n, r1,c1,r2,c2, k, m, c=100020001, flag=-1;
	
	scanf("%d%d%d%d", &r1,&c1,&r2,&c2);
	for(k=20001;k>0;k-=2){
		for(m=0;m<k;m++){
			if(m<=k/2){
				j+=flag;
			}
			else{
				i+=flag;
			}
			map[i][j]=c--;
		}
		flag*=-1;
	}
	for(i=5000+r1;i<=5000+r2;i++){
		for(j=5000+c1;j<=5000+c2;j++){
			printf("%d", map[i][j]);
		}
		puts("\n");
	}
	return 0;
}

