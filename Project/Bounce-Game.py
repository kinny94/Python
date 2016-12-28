from Tkinter import *
import random 
import time

tk = Tk()

tk.title("Bounce!!")
tk.resizable(0,0)	#size of the canvas can't be changed
tk.wm_attributes("-topmost", 1)	#To place the window containing our canvas in front of all other windows

#Initializing the canvas
canvas = Canvas(tk, width = 500, height = 500, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

class Ball:

	#function for initialization
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
		self.canvas.move(self.id, 245, 100)

	#function for animation
	def draw(self):
		#move function takes 3 arguements, !st = id, 2nd = how much you wanna move, 3rd = movement up or down
		self.canvas.move(self.id, 0, -1	)

ball = Ball(canvas, 'red')



#Loop to keep on updating the canvas, to always show the ball moving
while 1:
	ball.draw()
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)

tk.mainloop()