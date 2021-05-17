#include <stdio.h>
int main()
{
    int i, n, m, ret = 0;
    char *s;
    scanf("%d%d%s", &n, &m , s);
    for (i = 0; i < n; i++)
    {
        ret *= 2;
        if (s[i] == 'u')
            ret++;
        
    }
    while(m-- && ret)
        ret ^= ((ret<<1 & ((1 << n) - 1)) + (ret >> (n - 1) & 1)) ;    
    while(n--)
        printf("%c", ret & 1 << n ? 'u' : 'd');
}