A = []
for i in range(101):
	At = []
	for j in range(101):
		At.append(0)
	A.append(At)
for _ in range(4):
	lx, ly, rx, ry = map(int, input().split())
	for i in range(lx, rx):
		for j in range(ly, ry):
			A[i][j] = 1
ans = 0
for i in range(101):
	for j in range(101):
		ans += A[i][j]
print(ans)
