def hello(name = 'Jose'):
	print "Hello function executed!!"

	def greet():
		print "I am from inside the greet function!"
	
	def welcome():
		print "I am from inside the wwelcome function!"

	print greet()
	print welcome()
	print 'Back inside the hello function!'

	if name == "Jose":
		return greet #not the function call, but the entire function
	else:
		return welcome

hello()