def f(a, b, c):
	if a==b:
		return c
	if b==c:
		return a
	if c==a:
		return b

Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
print(f(Ax, Bx, Cx), f(Ay, By, Cy))