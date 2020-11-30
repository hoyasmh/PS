#include <stdio.h>

int chk[26];
int max, cnt, i, n, k;
char strs[51][16];
int g_cnt;
int read_chk(char *str)
{
    while (*str)
        if (!chk[*(str++) - 'a'])
            return 0;
    return 1;        
}

void sel_alpha(int m, int begin)
{
	int j;
	
	if (!m)
    {
    	g_cnt++;
        cnt = 0;
        i = -1;
        while (++i < n)
            cnt += read_chk(strs[i]);
        if (cnt > max)
            max = cnt;	    
    }   
    else
    {
    	for(j = begin;j < 26;j++)
    	{
    		if (!chk[j])
       		{
        		chk[j] = 1;
        		sel_alpha(m-1, j + 1);
        		chk[j] = 0;
        	}
        }
    }           
}

int main()
{
    chk[0] = 1;
    chk[2] = 1;
    chk[13] = 1;
    chk[8] = 1;
    chk[19] = 1;
    scanf("%d%d", &n, &k);
    if (k < 5) return (0);
    for (i = 0;i < n; i++)
        scanf("%s", strs[i]);
    sel_alpha(k-5, 0);
    printf("%d\n", max);
    return 0;    
}
