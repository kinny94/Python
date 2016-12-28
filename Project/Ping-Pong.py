from Tkinter import *
import random
import time

counter = 0
counter1 = 0

tk = Tk()
tk.title("Ping-Pong!!")
tk.resizable(0, 0)							#Won't be abnle to resize
tk.wm_attributes("-topmost", 1)				#Make it the topmost window
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.config(bg = "black")

canvas.pack()
tk.update()

canvas.create_line(250, 0, 250, 400, fill = "white")

class Ball:
	def __init__(self, canvas, color, paddle, paddle1):
		self.canvas = canvas
		self.paddle = paddle
		self.paddle1 = paddle1
		self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
		self.canvas.move(self.id, 230, 200)
		start = [-3, -2, -1, 0, 1, 2, 3]
		random.shuffle(start)
		self.x = start[0]
		self.y = -3
		self.canvas_height = self.canvas.winfo_height()
		self.canvas_width = self.canvas.winfo_width()
		
	def score(self, value):
		global counter
		global counter1

		if value == True:
			a = self.canvas.create_text(125, 40, text = counter, font = ("Arial", 60), fill = "Green")
			canvas.itemconfig(a, fill = "black")
			counter += 1
			a = self.canvas.create_text(125, 40, text = counter, font = ("Arial", 60), fill = "Green")

		if value == False:
			a = self.canvas.create_text(375, 40, text = counter1, font = ("Arial", 60), fill = "Yellow")
			canvas.itemconfig(a, fill = "black")
			counter1 += 1
			a = self.canvas.create_text(375, 40, text = counter1, font = ("Arial", 60), fill = "Yellow")



	def draw(self):
		self.canvas.move(self.id, self.x, self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <= 0:
			self.y = 3
		if pos[3] >= self.canvas_height:
			self.y = -3
		if pos[0] <= 0:
			self.x = 3
			self.score(True)
		if pos[2] >= self.canvas_width:
			self.x = -3
			self.score(False)
		if self.hit_paddle(pos) == True:
			self.x = 3
		if self.hit_paddle1(pos) == True:
			self.x = -3

	def hit_paddle(self, pos):
		paddle_pos = self.canvas.coords(self.paddle.id)
		if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
			if pos[0] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
				return True
			return False

	def hit_paddle1(self, pos):
		paddle_pos = self.canvas.coords(self.paddle1.id)
		if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
			if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
				return True
			return False


class Paddle:
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_rectangle(0, 150, 30, 250, fill = color)
		self.y = 0
		self.canvas_height = self.canvas.winfo_height()
		self.canvas_width = self.canvas.winfo_width()	
		self.canvas.bind_all("a", self.left)
		self.canvas.bind_all("d", self.right)

	def draw(self):
		self.canvas.move(self.id, 0, self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <= 0:
			self.y  =0
		if pos[3] >= 400:
			self.y = 0

	def left(self, evt):
		self.y = -3

	def right(self, evt):
		self.y = 3

class Paddle1:
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = canvas.create_rectangle(470, 150, 500, 250, fill = color)
		self.canvas_height = self.canvas.winfo_height()
		self.canvas_width = self.canvas.winfo_width()	
		self.y = 0
		self.canvas.bind_all("<KeyPress-Left>", self.left)
		self.canvas.bind_all("<KeyPress-Right>", self.right)

	def draw(self):
		self.canvas.move(self.id, 0, self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <= 0:
			self.y = 0
		if pos[3] >= 400:
			self.y = 0

	def left(self, evt):
		self.y = 3

	def right(self, evt):
		self.y = -3

paddle = Paddle(canvas, "yellow")
paddle1 = Paddle1(canvas, "Green")
ball = Ball(canvas, "orange", paddle, paddle1)

while 1:
	ball.draw()
	paddle.draw()
	paddle1.draw()
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)

	if counter == 10:
		ball.x = 0
		ball.y = 0
		paddle.y = 0
		paddle1.y = 0
		canvas.create_text(250, 200, text = "Congrats Player Green! You Win!", font = 32, fill = "Green")
		canvas.create_text(250, 215, text = "Score: " + str(counter) + " : " + str(counter1), font = 32, fill = "red")

	if counter1 == 10:
		ball.x = 0
		ball.y = 0
		paddle.y = 0
		paddle1.y = 0
		canvas.create_text(250, 200, text = "Congrats Player Yellow! You Win!", font = 32, fill = "Yellow")
		canvas.create_text(250, 215, text = "Score: " + str(counter) + " : " + str(counter1), font = 32, fill = "red")
		

tk.mainloop()