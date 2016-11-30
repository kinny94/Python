import sys

print "The module will read, till you press enter"
inputStatement = sys.stdin.readline()
print inputStatement

print "\n"


print "The module will read the first 10 characters, till you press enter"
inputStatement2 = sys.stdin.readline(10)
print inputStatement2

sys.stdout.write("This  staatement is written using sys.stdout.write")

print sys.version	
