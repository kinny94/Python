import Tkinter
import tkMessageBox

root = Tkinter.Tk()

tkMessageBox.showinfo("Title ", "Something went wrong!!	")
answer = tkMessageBox.askquestion("Question 1:", "Are you a human?")

if answer == "yes":
	tkMessageBox.showinfo("Congrats!!", "Well Duh!!")

if answer == "no":
	tkMessageBox.showinfo("Nope!!", "You are an alien!!")

root.mainloop()