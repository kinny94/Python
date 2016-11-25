class Book(object):

	#first special method
	def __init__(self, title,author, pages):
		self.title = title
		self.author = author
		self.pages = pages

	#second specia method, when print function is called __str__ method is called
	def __str__(self):
		return "Title: %s, Author: %s, Pages: %s" %(self.title, self.author, self.pages)

	def __len__(self):
		return self.pages

	def __del__(self):
		print "A book is gone"

x = Book("My Book", "Arjun Dass", 560)
print x	