from Tkinter import *
root  = Tk()

label1 = Label(root, text='Label')
label2 = Label(root, text="Label2")
label3 = Label(root, text="Label3")

entryspace1 = Entry(root)
entryspace2 = Entry(root)
entryspace3 = Entry(root)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)

entryspace1.grid(row=0, column=1)
entryspace2.grid(row=1, column=1)
entryspace3.grid(row=2, column=1)

root.mainloop()
