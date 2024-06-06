#include <stdio.h>

int N, A[8010];

int main(void)
{
	scanf("%d", &N);
	for(int i=0; i<N; i++)
		scanf("%d", &A[i]);
	int ans = 0;
	for(int i=0; i<N; i++)
		for(int j=i+1; j<N; j++)
			if((A[i]+A[j])%3==0)
				ans += 1;
	printf("%d\n", ans);

	return 0;
}
