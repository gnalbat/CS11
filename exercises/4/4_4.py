t = int(input())

while t > 0:
	A = int(input())
	B = int(input())
	C = int(input())

	if C == 0 or (C > 0 and A > B) or (C < 0 and A < B):
		print("Invalid Input!")
		print()

	else:
		if A > B and C < 0:
			B -= 1
		else:
			B += 1
		for i in range(A, B, C):
			if i % 3 == 0 and i % 5 == 0:
				print("FizzBuzz")
			elif i % 5 == 0:
				print("Buzz")
			elif i % 3 == 0:
				print("Fizz")
			else:
				print(i)
		print()
	t -= 1
