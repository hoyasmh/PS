#include <stdio.h>
#include <string.h>
int chk[10000000];
int _pow(int n)
{
    int ret = 10;
    while(--n)
        ret *= 10;
    return ret;
}

int period(int *idx, int m, int n)
{
    int mod = _pow(n);
    long long temp = m % mod;
    m = (int)temp;
    memset(chk, 0, sizeof(chk));
    *idx = 1;
    while (1)
    {
        if (chk[temp])
            return chk[temp];
        chk[temp] = (*idx)++;
        temp = temp * m % mod;
    }
    return 0;
}

int mypow(int num, int exp, int start, int end)
{
    long long ret = 1;
    while(exp)
    {
        if (exp & 1)
            ret = (ret * num) % mod;
        num = (num * num) % mod;
        exp /= 2;
    }
    return ret;
}

int main()
{
   
    int b, n, i, j,start, end, ans;
    scanf("%d", &b);
    while(b)
    {
        scanf("%d%d", &i, &n);
        ans = b;
        start = period(&end, b, n);
        for (j = 0; j < i - 1; j++)
        {
            ans = start + (ans - start) % (end - start);
            ans = mypow(b, ans, end - start);            
        }
        ans %= _pow(n);
        printf("%d\n", ans);
        scanf("%d", &b);
    }  
}