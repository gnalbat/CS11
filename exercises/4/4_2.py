t = int(input())

while t > 0:
	s = int(input())
	i = 0
	while i < s:
		print((s - i - 1) * ' ' + (2*i + 1)* '*')
		i += 1
	i = 1
	while i < s:
		print(i * ' ' + (2*(s - i) - 1) * '*')
		i += 1
	print()
	t -= 1
