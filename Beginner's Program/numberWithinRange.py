def ran_check(num, low, high):
	if num in range(low, high):
		print " %s is in the range " %str(num)
	else:
		print " The number is outside the range."

ran_check(5, 1, 7)