file1 = open("Test.txt", "r")
print file1.read()

#The following code will not print anything.
print file1.read()

# This is because of the cursor. The cursor is now at the end off the file.
# The following method will tell you the location of the cursor.
print file1.tell()

#The following code will reset the cursor position
file1.seek(0,0)
print file1.read()
file1.seek(0,0)
print "\n"

#The following code will print the first x characters in the text file
print file1.read(21)
#Again we need to reset the cursor position
file1.seek(0,0)
print "\n"
print file1.read()
