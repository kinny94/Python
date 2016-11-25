def exception():
	try:
		print 2 + "Arjun"
	except:
		print "Cannot Add an integer and a string!! \n"


def exception2():
	try:
		print 2 + "Arjun"
	except:
		print "Cannot Add an integer and a string!!"
	finally:
		print "I am from finally block\n"

def exception3():
	try:
		x = 2+2
		print "Try block x is %s"%(x)
		print "This code is written in try block!!\n"
	except:
		print "I wont'be reached!!\n"
	finally:
		print "The value of x is : %s" %(x)

exception()
exception2()
exception3()


