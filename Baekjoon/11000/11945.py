N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(input())
for i in range(N):
    for j in range(M-1, -1, -1):
        print(A[i][j], end="")
    print()
