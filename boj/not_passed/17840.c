#include <stdio.h>
#include <string.h>
int ret[2][2]
int matsq(int arr[][2], int brr[][2])
{
    memset(ret, 0, sizeof(ret))
    int i, j, k;
    for (i = 0; i < 2; i++)
        for (j = 0; j < 2; j++)
            for (k = 0; k < 2; k ++)
                ret[i][j] = (ret[i][j] + arr[i][k] * brr[k][j]) % m          
}
int fib(int n, int m)
{
    int fb[2][2] = {{1, 1}, {1, 0}}, ans = {{1, 0}, {0, 1}}
}