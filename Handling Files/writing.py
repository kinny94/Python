file1 = open("Test.txt", "w")
try:
	file1.read()
except: 
	print "You can't read,  cause you are using the write parameter!!"

file1.write("This is the ttest line to be written into the text file")
#we need to  close the file aafter writing in it
file1.close()


file2 = open("Test.txt", "r")
print file2.read()
#If the file already exists in the folder, the file will be rewritten
# To avoid this, we need to append
# you can both write and read using wb+ 