def isPalindrome(s):
	for i in range(len(s)//2):
		if s[i]!=s[len(s)-i-1]:
			return 0
	return 1
	
s = input()
print(isPalindrome(s))
