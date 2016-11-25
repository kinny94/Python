def writeFile():
	try:
		f = open('NewFile', 'w')
		f.write("Text to be written in NewFile")
	except:
		print "There was an error writing into the file"
	else:
		print "File has been written succesfully"

def writeFile2():
	try:
		f = open('NewFile', 'w')
		f.write("Text to bee written in NewFile from 2nd function!")
	except:
		print "There was an  error writing into the file!!"
	else:
		print "File written Success 2"
	finally:
		print "I am from finally block, I will always appear!!"

def readFile():
	try:
		f = open('NewFile2', 'r')
		f.write("This won't be written if the file do not exists!")
	except:
		print "Intentional Error!!. There is not file wwith such name!"
	else:
		print "Written to the  file!!"
	finally:
		print "Hello!! I am 'finally' here!!"

def takeInput():
	while True:
		try:
			print "Enter an Integer!!"
			val = int(raw_input("Please enter an integer : "))
		except:
			print "You didn't enter anything!!"
			continue
		else:
			print "Yup, That is an Integer!"
			break
		finally:
			print "Guess Where I am From if I Will always appear!!"
		print val

writeFile()
writeFile2()
readFile()
takeInput()