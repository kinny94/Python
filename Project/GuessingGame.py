import random

var = random.randint(0,20)
x = 5
print "Guess the number, you have 5 chances:"
while True:
	guess = input("Enter your guess between 0 - 20: ")

	if(x>1): 
		if guess<var:
			print "Its bigger than %s"%(guess)
			x -= 1
		elif guess>var:
			print "Its smaller than %s"%(guess)
			x -= 1
		else:
			print "Yep, You got it right. The number is %s"%(var)
			break
	else:
		print "You ran out of chances!!"
		break
