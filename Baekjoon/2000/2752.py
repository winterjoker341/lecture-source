a, b, c = map(int, input().split())
mx = max(max(a, b), c)
mn = min(min(a, b), c)
print(mn, a+b+c-mx-mn, mx)
