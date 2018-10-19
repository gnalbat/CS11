t = int(input())

while t > 0:
	a = int(input())
	n = int(input())
	i = 1
	
	if a > n: 
		z = n 
	else: 
		z = a
	for j in range(1, z + 1):
		if((a % j == 0) and (n % j == 0)):
			gcd = j
			
	if gcd != 1:
		print("DOES NOT EXIST")
	else:
		while (a * i) % n != 1:
			i += 1
			if (a * i) % n == 1:
				break
		print(i)
		
	t -= 1