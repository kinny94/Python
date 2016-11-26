#alllows you to keep count as  you iterate
l = ['a', 'b', 'c']
count = 0
for item in l:
	print item
print "\n"

for count, item in enumerate(l):
	print count
	print item
print "\n"

for count, item in enumerate(l):
	if count >= 2:
		break
	else:
		print item
print "\n"