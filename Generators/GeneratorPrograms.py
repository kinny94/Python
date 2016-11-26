#generate the square of numbers up to some number n

def genSquare(n):
	for i in range(n):
		yield i ** 2

for x in genSquare(10):
	print x

#generates n random numbers  between a low and a  high number
import random
def rand_num(low, high,n):
	for i in range(n):
		yield random.randomint(low, high)

for num in rand_num(1, 10, 12):	
	print num

#iter function to convert the string
s= 'helllo'
s = iter(s)
print next(s)

my_list = [1,2,3,4,5]
gencomp = (item for item in my_list if item > 3)

for item in gencomp:
	item