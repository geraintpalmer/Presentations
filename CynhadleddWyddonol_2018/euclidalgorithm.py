a = 1071
b = 462
C = []

while a != 0 and b != 0:
	i = 0
	while a >= b:
		a -= b
		i += 1
	a, b = b, a
	C.append(i)
C.append(a)
C.append(b)

print(max(C))