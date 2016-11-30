file1 = open("Test.txt", "a")
file1.write("\nThis text will be appendedto the existing file")
file1.close()

file1 = open("Test.txt", "r")
print file1.read()	

#No rocket science in this file