from Tkinter import *
root = Tk()

def printName():
	print "Hello, My name is Arjun Dass!!"

label1 = Label(root, text="Name")
label2 = Label(root, text="Password")
name = Entry(root)
password = Entry(root)

label1.grid(row=0, column="0", sticky= "E")
name.grid(row=0, column="1")
label2.grid(row=1, column="0", sticky="E")
password.grid(row=1, column="1")

cbutton = Checkbutton(root, text="Remember Me! ")
cbutton.grid(columnspan=2)

submit = Button(root, text="Submit", fg="Cyan", bg="Blue", command=printName)
submit.grid(columnspan=2)

root.mainloop()