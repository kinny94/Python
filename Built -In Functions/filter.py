def even_check(num):
	if num % 2  == 0:
		print "Yes it is an even number"
	else:
		print "Its an odd number"

lst = range(10)
print lst
print filter(even_check, lst)
print "\n"

print "The following is using the lambda function"
print filter(lambda num: num % 2 == 0, lst)

