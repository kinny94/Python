z = [1, 2, 3]
y = [4, 5, 6]
print z
print y 
print  "\n"

print zip(z, y)

for pair in zip(z, y):	
	print max(pair)
print "\n"

print "The following is using the lambda function!!"
print map(lambda pair:max(pair), zip(z, y))
print "\n"

d1 = {'a':1, 'b':2}
d2 = {'c':4, 'd':5}

print zip(d1, d2)
print zip(d2, d1.itervalues())
print "\n"

print "Not using a function"
def switcharoo(d1, d2):
	dout = {}

	for d1key, d2val in zip(d1, d2.itervalues()):
		dout[d1key] = d2val

	return dout
print d1
print d2
switcharoo(d1, d2 )