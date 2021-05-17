#include <stdio.h>
long long fib[73] = {1, 2,}, n = 2, m, t, ans;
long long find(long long n){
    long long i = -1;
    while(fib[++i] <= n)
        if (fib[i] == n) return n;
    return i;
}
int main()
{
    while(fib[n - 1] <= 1.0e15){
        fib[n] = fib[n -1 ] + fib[n - 2];
        n++;
    }
    scanf("%lld", &m);
    t = m;
    while ((ans = find(m)) != m){
        m -= fib[ans-1];
    }
    printf("%lld\n", t == ans ? -1 : ans);
}