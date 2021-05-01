#include <stdio.h>
#define ABS(a, b) ((a > b) ? a - b : b - a) 
int msb(int n)
{
    if (!n)
        return 0;
    int i = 19;
    while((n & 1 << i) == 0)
        i--;
    return i;
}

int main()
{
    int n, k, mbit, cnt = 0;
    scanf("%d%d", &n, &k);
    if (n >= k)
        printf("%d\n", n - k);
    else
    {
        mbit = msb(n);
        while (mbit != msb(k))
        {
            if (k & 1)
            {
                k--;
                cnt++;
            }
            else
                k /= 2;
        }
        printf("%d %d\n", cnt , ABS(n, k));
    }
    return 0;
}
    