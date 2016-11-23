def unique_list(l):
	x = []
	for a in l:
		if a not in x: 
			x.append(a)
	return x

unique_list([1,1,1,1,1,2,2,3,4,5,5,5])