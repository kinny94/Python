fileName = raw_input("\nEnter you file name: ");
print fileName

fileName = fileName + ".txt"
print fileName	
fileName = open(fileName, "w")
fileName.write("Hello")
fileName.close()

file1 = open(fileName, "r")

file2 = open("copiedDFile.txt", "w")
file2.write(file1.read())
file2.close()
file1.close()

file2 = open("copiedFile.txt", "r")
print file2.read()