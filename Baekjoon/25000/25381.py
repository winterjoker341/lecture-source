s = input()
chk = [0 for _ in range(len(s))]
ans = 0
pos = 0
for i in range(len(s)):
	if s[i]=='B':
		pos = max(pos, i+1)
		for j in range(pos, len(s)):
			if s[j]=='C' and chk[j]==0:
				ans += 1
				chk[i] = chk[j] = 1
				break
			pos += 1
pos = 0
for i in range(len(s)):
	if s[i]=='A':
		pos = max(pos, i+1)
		for j in range(pos, len(s)):
			if s[j]=='B' and chk[j]==0:
				ans += 1
				chk[i] = chk[j] = 1
				break
			pos += 1
print(ans)
