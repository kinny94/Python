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
	def __init__(self, canvas, paddle, color):
		self.canvas = canvas
		self.paddle = paddle
		self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
		self.canvas.move(self.id, 245, 100)
		start = [-3, -2, -1, 0, 1, 2, 3]
		random.shuffle(start)
		self.x = start[0]
		self.y = -5
		self.canvas_height = self.canvas.winfo_height()
		self.canvas_width = self.canvas.winfo_width()	
		self.hit_bottom = False;

	def hit_paddle(self, pos):
		paddle_pos = self.canvas.coords(self.paddle.id)
		#pos[2] = ball's x coordinate paddle_pos[0] =  paddle's left side
		if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
			#pos[3] = bottom of the ball paddle_pos[1] = top of the paddle
			if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
				return True
			return False

	#function for animation
	def draw(self):
		#move function takes 3 arguements, !st = id, 2nd = how much you wanna move, 3rd = movement up or down
		self.canvas.move(self.id, self.x, self.y)
		#coords return an array with [x1, y1, x2, y2]
		pos = self.canvas.coords(self.id)	#we are getting the current coordinates
		#print(pos)
		if pos[1] <= 0:
			self.y = 3
		if pos[3] >= self.canvas_height:
			self.hit_bottom = True
			canvas.create_text(245, 100, text = "Game Over!!")
		if pos[0] <= 0:
			self.x =3 
		if pos[2] >= self.canvas_width:
			self.x = -3
		if self.hit_paddle(pos) == True:
			self.y = -3

class Paddle: 
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
		self.canvas.move(self.id, 200, 300)
		self.x = 0
		self.canvas_width = self.canvas.winfo_width()
		self.canvas.bind_all('<KeyPress-Left>', self.left)
		self.canvas.bind_all('<KeyPress-Right>', self.right)

	def draw(self):
		self.canvas.move(self.id, self.x, 0)
		pos = self.canvas.coords(self.id)
		if pos[0] <= 0:
			self.x = 0
		if pos[2] >= self.canvas_width:
			self.x = 0 

	def left(self, evt):
		self.x = -2

	def right(self, evt):
		self.x = 2

paddle = Paddle(canvas, 'gray')
ball = Ball(canvas, paddle, 'red')

#Loop to keep on updating the canvas, to always show the ball moving
while 1:
	if ball.hit_bottom == False:
		ball.draw()
		paddle.draw()
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)

tk.mainloop()