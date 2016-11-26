#map 
def farenheit(t):
	return (9.0/5) * t + 32

temp = [0, 225, 40, 100]
print map(farenheit, temp)

print "The following one is usiing the lambda function!!"

print map(lambda T: (9.0/5) * T + 32, temp)
print "\n"

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

print a
print b
print c
print "\n"

print "Just adding the first elements of the first two lists!!"
print map(lambda x,y: x+y, a,b)
print "\n"

print "Addind the elements of all the lists"
print map(lambda x,y,z: x+y+z, a,b,c)
