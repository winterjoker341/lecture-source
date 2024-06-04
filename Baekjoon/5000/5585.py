N = 1000-int(input())
costs = [500, 100, 50, 10, 5, 1]
ans = 0
for cost in costs:
	ans += N//cost
	N %= cost
print(ans)
