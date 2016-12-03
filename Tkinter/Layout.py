from Tkinter import *

root = Tk()

topFrame  = Frame(root)
topFrame.pack()

botFrame = Frame(root)
botFrame.pack()

label1 = Label(topFrame, text="This is a window!!")
label1.pack()

label2 = Label(botFrame, text="This is the bottom Frame!!")
label2.pack()

button1  = Button(botFrame, text="Click Me!!", fg="Blue")
button1.pack()

button2 = Button(topFrame, text="Don't Click Me!!", fg="Red", bg="Black")
button2.pack()

root.mainloop()