def up_low(s):
	d = {"upper":0, "lower":0}
	for c in s:
		if c.isupper():
			d["upper"]+=1
		elif c.islower():
			d["lower"]+=1
		else:
			pass
	print "Original String : ", s
	print "No. of Upper case Characters	: ", d["upper"]
	print "No. of Lower case Characters : ", d["lower"]

s = "Hello, My name is Arjun Dass"
up_low(s)