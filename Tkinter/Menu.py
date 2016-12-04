import Tkinter
root = Tkinter.Tk()
root.geometry("500x500")

def random():
	print "This is a random statement"

mainMenu = Tkinter.Menu(root)
root.configure(menu = mainMenu)

subMenu = Tkinter.Menu(mainMenu)

mainMenu.add_cascade(label="File", menu = subMenu)

subMenu.add_command(label = "Random Func", command = random)
subMenu.add_separator()
subMenu.add_command(label = "New File", command = random)
subMenu.add_separator()
subMenu.add_command(label = "Open", command = random)

root.mainloop()
