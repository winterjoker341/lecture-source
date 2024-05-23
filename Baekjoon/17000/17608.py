N = int(input())
A = []
for i in range(N):
	A.append(int(input()))
H = 0
ans = 0
for i in range(N-1, -1, -1):
	if A[i]>H:
		H = A[i]
		ans += 1
print(ans)
