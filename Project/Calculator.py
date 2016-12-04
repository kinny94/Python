from Tkinter import *

root = Tk()

equalTo = ""

def btnPress(num):
	global equalTo
	equalTo = equalTo + str(num)
	equation.set(equalTo)

def equalPress():
	global equalTo
	total = str(eval(equalTo))
	equation.set(total)
	equalTo = ""

def clear():
	global equalTo
	equalTo = ""
	equation.set("Let's Calculate!")

zero  = Button(root, text = "0", command = lambda: btnPress(0))
zero.grid(row = 4, column = 1)
one   = Button(root, text = "1", command = lambda: btnPress(1))
one.grid(row = 1, column = 0)
two   = Button(root, text = "2", command = lambda: btnPress(2))
two.grid(row = 1, column = 1)
three = Button(root, text = "3", command = lambda: btnPress(3))
three.grid(row = 1, column = 2)
four  = Button(root, text = "4", command = lambda: btnPress(4))
four.grid(row = 2, column = 0)
five  = Button(root, text = "5", command = lambda: btnPress(5))
five.grid(row = 2, column = 1)
six   = Button(root, text = "6", command = lambda: btnPress(6))
six.grid(row = 2, column = 2)
seven = Button(root, text = "7", command = lambda: btnPress(7))
seven.grid(row = 3, column = 0)
eight = Button(root, text = "8", command = lambda: btnPress(8))
eight.grid(row = 3, column = 1)
nine  = Button(root, text = "9", command = lambda: btnPress(9))
nine.grid(row = 3, column = 2)

plus     = Button(root, text="+", command = lambda: btnPress("+"))
minus    = Button(root, text="-", command = lambda: btnPress("-"))
divide   = Button(root, text="/", command = lambda: btnPress("/"))
multiply = Button(root, text="*", command = lambda: btnPress("*"))
equal    = Button(root, text="=", command = equalPress)
clear    = Button(root, text="C", command = clear)

plus.grid(row = 1, column = 3)
minus.grid(row = 2, column = 3)
multiply.grid(row = 3, column = 3)
divide.grid(row = 4,column = 3 )
equal.grid(row = 4, column = 2)
clear.grid(row = 4, column = 0)



#String var to update the text of the label 
equation = StringVar()

calculation = Label(root, textvariable = equation)

equation.set("Let's Calculate!")

calculation.grid(row=0,columnspan = 4)

root.mainloop()