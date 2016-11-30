class Parent:
	def func(self):
		print "Hello"

	def PChild(self):
		print "Child will access me!!"

class Child(Parent):
	def func(self):
		print ("This is a chld function!!")

c =  Child()
c.func()
c.PChild()