class Father(object):

	fatherVariable = 5
	def __init__(self):
		print "I am the father!!"

	def WhoAmI(self):
		print "Dad!!"

	def doing(self):
		print "Dad is eating!!"

class Son(Father):

	sonVariable = 1
	def __init__(self):
		print "I am the son!!"
		Father.__init__(self)

	def WhoAmI(self):
		print "Son!!"

	def doing(self):
		print "Watching dad eating food!!"

	def studying(self):
		print "Nope!!, not studying at all!!"

d = Son()
d.WhoAmI()
print "I am a variable from the father's class: %s" %(d.fatherVariable)
print "I am a variable from the son's class: %s" %(d.sonVariable)