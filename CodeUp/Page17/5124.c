#include <stdio.h>

int N, t;
long long A[13];

int main(void)
{
	scanf("%d", &N);
	for(int i=0; i<N; i++) {
		scanf("%d", &t);
		A[t%3]++;
	}
	printf("%lld\n", A[0]*(A[0]-1)/2+A[1]*A[2]);

	return 0;
}
