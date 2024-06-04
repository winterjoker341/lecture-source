def my_sum(n):
	res = n
	while n>0:
		res += n%10
		n = n//10
	return (res if res<=10000 else 0)

chk = []
for i in range(10010):
	chk.append(i)
for i in range(1, 10001):
	chk[my_sum(i)] = 0
for i in range(1, 10001):
	if chk[i]:
		print(i)
