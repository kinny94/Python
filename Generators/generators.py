def genCubes(n):
	for num in range(n):
		yield num**3

for x in genCubes(10):
	print x

print "\n"

print "Fibonacci Normally"

def fibo(n):
	a = 1
	b = 1
	output = []
	for i in range(n):
		output.append(a)
		a,b = b, a+b
	print output

fibo(10)

print "\n"
print "Fibonacci using Generators"

def genFibo(n):
	a = 1
	b = 1
	for i in range(n):
		yield a
		t = a
		a = b
		b = t + b

for num in genFibo(10):
	print num