#include <stdio.h>

int arr[100001];

int main()
{
    int i, n, m, k, cnt;
    scanf("%d%d", &n, &k);
    i = 0;
    cnt = 0;
    m =n;
    putchar('<');
    while(m)
    {
        if(arr[i] == 0)
        {
            cnt++;
            if(cnt == k)
            {
                arr[i] = 1;
                m--;
                printf("%d", i+1);
                if(m > 0)
                	printf(", ");
                cnt = 0;
            }
        }
        i = (i + 1) % n;
    }
    putchar('>');
    return 0;  
}
