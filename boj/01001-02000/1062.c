#include <stdio.h>

int chk[26];
int max, cnt, i, n, k;
char strs[51][16];
int read_chk(char *str)
{
    while (*str)
        if (chk[*(str++) - 'a'])
            return 0;
    return 1;        
}

int count(int *arr)
{
	int i, cnt;
	
	i = -1;
	cnt = 0;
	while(++i < 26)
		if (arr[i])
			cnt++;
	return cnt;		
}

void valid_alpha(char *str)
{
	while(*str)
		chk[*(str++) - 'a'] = 1;
}

void sel_alpha(int m, int begin)
{
	int j;
	
	if (!m)
    {
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
    		if (chk[j])
			{	
        		chk[j] = 0;
        		sel_alpha(m-1, j + 1);
        		chk[j] = 1;
        	}
        }
    }           
}

int main()
{
    scanf("%d%d", &n, &k);
    if (k < 5)
	{
		printf("%d\n", 0);
		return (0);
	}
    for (i = 0;i < n; i++)
    {
        scanf("%s", strs[i]);
        valid_alpha(strs[i]);
    }
    chk[0] = 0;
    chk[2] = 0;
    chk[13] = 0;
    chk[8] = 0;
    chk[19] = 0;
    if(k-5 >= count(chk))
    {
    	printf("%d\n", n);
    	return 0;
    }
    sel_alpha(k-5, 0);
    printf("%d\n", max);
    return 0;    
}
