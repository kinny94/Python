def primeOrNot(num):
	for n in range(2, num):
		if num % n == 0: 
			print "Not a prime number!!"
			break
	else:
		print "Yes It is a prime number!!"

primeOrNot(13)