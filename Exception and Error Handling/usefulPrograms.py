# error in a for loop

def problem1():
	try:
		for i in ['a', 'b', 'c']:
			print i**2
	except:
		print "An error occured!!"

problem1()

def problem2():
	x = 5
	y = 0
	try:
		z = x/y
	except:
		print "Cannot devide by zero"
	else:
		print "Value of z is %s"%(z)
	finally:
		print "All Done Here 'finally'!"

problem2()

#error handling and printing square

def problem3():
	while True:
		try:
			val = int(raw_input("Please enter an integer: "))
		except:
			print "Please enter an integer!!"
			continue
		else:
			print "You enetered %s"%(val)
			print "The square of %s is %s"%(val,val**2)
			break
		finally:
			print "Finally"

problem3()