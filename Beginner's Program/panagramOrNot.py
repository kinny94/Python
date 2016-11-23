import string 
def isPangram(string1, alphabet=string.ascii_lowercase):
	alphaset = set(alphabet)
	return alphaset <= set(string1.lower())

isPangram("The quick brown foox jumps the lazy dog")
