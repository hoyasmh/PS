#include <stdio.h>

int dig(int n)
{
	while(n /10)
		n = n / 10 + n % 10;
	return n;
}

int main()
{
	long long t, k, m ,i, x, y, temp;

	scanf("%lld", &t);
	while(t--)
	{	
		scanf("%lld%lld", &k, &m);
		m = dig(m);
		i = 0;
		x = 0;
		y = 1;
		temp = 1;
		while(++i < k)
		{
			if(i % 4 == 1)
				x += (temp = dig(temp * m));
			else if(i % 4 == 2)
				y -= (temp = dig(temp * m));
			else if(i % 4 == 3)
				x -= (temp = dig(temp * m));
			else
				y += (temp = dig(temp * m));
		}
		printf("%lld %lld\n", x, y);
	}
	return 0;
}


