#include <stdio.h>
int main()
{
    char chk[1000001] = {0, 1,};
    int i, j, t, n;
    
    for (i = 2; i < 1000001; i++)
    {
        j = 1;
        while (i - j * j >= 0)
        {
            if (chk[i - j * j] == -1 || i - j * j == 0)
            {
                chk[i] = 1;
                break;
            }
            j++;
        }
        if (!chk[i])
            chk[i] = -1;         
    }
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        printf("%s\n", chk[n] == 1? "koosaga" : "cubelover");
    }
    return 0;
}
    
