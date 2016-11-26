#decorators are function for functions

s = 'This is a global variable!!'
def func():
	print locals()
	print globals()
	print globals()['s']

func()

def hello(name = "Arjun"):
	print 'hello ' + name

hello()
greet = hello
greet()
del hello
print "hello function deleted!!"
try:
	hello()
except:
	print "Hello function do not exists!"
finally:
	print "Greet function still exists!!"
	greet()