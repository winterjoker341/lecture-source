#include <stdio.h>

int N, A[10010];

int main(void)
{
	scanf("%d", &N);
	for(int i=1; i<=N; i++)
		scanf("%d", &A[i]);
	int ans = 0;
	for(int i=1; i<=N; i++)
		if(A[i-1]==0 && A[i]==0 && A[i+1]==0)
			ans += 1;
	printf("%d\n", ans);

	return 0;
}
