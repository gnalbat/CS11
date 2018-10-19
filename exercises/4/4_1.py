t = int(input())

while t > 0:
	n = int(input())
	for i in range(1, n + 1):
		line = ""
		for j in range(1, n + 1):
			line = line + str(i*j) + "\t"
		print(line.rstrip())
	print()
	t -= 1
