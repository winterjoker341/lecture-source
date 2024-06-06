#include <stdio.h>

long long a, b, r, c, d;

int main(void)
{
	scanf("%lld%lld%lld%lld%lld", &a, &b, &r, &c, &d);
	long long p = (a-c)*(a-c)+(b-d)*(b-d);
	long long q = r*r;
	if(p<q)
		puts("in");
	else if(p==q)
		puts("on");
	else
		puts("out");

	return 0;
}
