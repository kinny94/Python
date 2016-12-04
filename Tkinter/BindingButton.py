from Tkinter import *

root = Tk()

def leftClick(event):
	print "Left mouse button clicked!!"

def rightClick(event):
	print "Right mouse button clicked!!"

def mouseScroll(event):
	print "Mid mouse button clicked!!"

def left(event):
	print "Left Key Pressed!!"

def right(event):
	print "Right key pressed!!"

def up(event):
	print "Up Key Pressed!!"

def bottom(event):
	print "Buttom key pressed!!"

root.geometry("500x500")
root.bind("<Button-1>", leftClick)
root.bind("<Button-2>", mouseScroll)
root.bind("<Button-3>", rightClick)
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>",up)
root.bind("<Down>", bottom)
 
root.mainloop()