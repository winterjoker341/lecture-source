#include <stdio.h>

int N, map[110];
char s[100010], ans[100010];

int main(void)
{
	scanf("%d %s", &N, s);
	map['A'] = 'U', map['T'] = 'A';
	map['C'] = 'G', map['G'] = 'C';
	for(int i=0; i<N; i++)
		ans[i] = map[s[i]];
	puts(ans);

	return 0;
}
