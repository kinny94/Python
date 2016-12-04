from Tkinter import *

root = Tk()
root.geometry("200x200")

welcome = Label(root, text="Do your calculations here!!")
welcome.pack()

def evaluate(event):
	data = e.get()
	ans.configure(text = "Answer " + str(eval(data)))

e = Entry(root)

e.bind("<Return>", evaluate)
e.pack()

ans = Label(root)
ans.pack()

root.mainloop()