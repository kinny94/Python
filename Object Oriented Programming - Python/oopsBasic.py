# Creating My First Class

class MyFirstClass(object):
	name = 'Arjun Dass'

	def __init__(self, college, var, boole = "True"):
		self.college = college
		self.newVariable = "I am a new variable!!"
		self.var = var
		self.boole= boole

a = MyFirstClass(college = "Stevens Institute of Technology", var = "Justice")
print "********************** First Class *************** \n"
print a.name 
print a.college 
print a.newVariable
print a.var
print a.boole


