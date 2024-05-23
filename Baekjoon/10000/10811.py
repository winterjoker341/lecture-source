N, M = map(int, input().split())
A = []
for i in range(N+1):
	A.append(i)
for i in range(M):
	a, b = map(int, input().split())
	for j in range(a, (a+b)//2+1):
		A[j], A[a+b-j] = A[a+b-j], A[j]
for i in range(1, N+1):
	print(A[i], end=' ')
