import math

n = int(input())
M = {}
ans = 0
for i in range(n):
	x, y = map(int, input().split())
	if x!=0 or y!=0:
		k = math.gcd(x, y)
		if (x//k, y//k) not in M:
			M[(x//k, y//k)] = 1
		else:
			M[(x//k, y//k)] += 1
		ans = max(ans, M[(x//k, y//k)])
print(ans)