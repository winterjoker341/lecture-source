N = n = int(input())
ans = 0
while True:
	ans += 1
	n = t = (n%10)*10+(n//10+n%10)%10
	if N==t:
		break
print(ans)
