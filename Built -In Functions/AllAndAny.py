l = [True, False, False, True]
x = all(l)
if x == True:
	print "All true"
else:
	print "Not All true"
print "\n"

y = any(l)
if y == True:
	print "There is atleast one true"
else:
	print "There are no true"