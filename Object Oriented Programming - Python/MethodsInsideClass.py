class Circle(object):
	pi = 3.14

	def __init__(self):
		self.radius = 5

	def get_radius(self):
		return self.radius

	def set_radius(self, newRadius):
		self.newRadius = newRadius;
		self.radius = self.newRadius
		return self.radius
		

	def get_area(self):
		self.area = (self.radius**2) * 3.14
		return self.area

	def get_perimeter(self):
		self.perimeter = 2 * Circle.pi * self.radius
		return self.perimeter

obj = Circle()

pie =  obj.pi
print "Value of pie %s" %(pie)

getRadius =  obj.get_radius()
print "Current radius is %s" %(getRadius)

getArea =  obj.get_area()
print "The area with radius %s is %s" %(obj.radius, getArea)

x =  obj.get_perimeter()
print "The perimeter is %s" %(x) 

setRadius =  obj.set_radius(7)

print "The new radius is %s" %(obj.get_radius())

print "The new area with radius %s is %s" %(obj.get_radius(), obj.get_area())

print "The new perimeter with radius %s is %s" %(obj.get_radius(), obj.get_perimeter())