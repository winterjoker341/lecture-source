import sys
input = sys.stdin.readline
	
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = {}
for i in range(m):
	M[B[i]] = 1
ans = []
for i in range(n):
	if A[i] not in M:
		ans.append(A[i])
if len(ans)==0:
	print("0")
else:
	ans.sort()
	print(len(ans))
	for i in range(len(ans)):
		print(ans[i], end=' ')
