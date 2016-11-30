import turtle
t = turtle.Pen()
t.forward(50)
t.left(90)

t.reset()

for i in range(0, 8):
	t.forward(50)
	t.left(45)

t.reset()

for i in range(1, 38):
	t.forward(100)
	t.left(175)

t.reset()

for i in range(1, 20):
	t.forward(100)
	t.left(95)

t.right(90)
t.forward(100)
for i in range(1, 20):
	t.forward(100)
	t.left(95)

t.reset()
t.left(180)
t.forward(100)
t.right(180)

for i in range(1, 20):
	t.forward(100)
	t.left(95)

t.up()
t.forward(100)
t.forward(40)
t.down()
for i in range(1, 20):
	t.forward(100)
	t.left(95)

t.reset()

t.color(0, 0, 1)
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(30)
t.left(90)
t.forward(40)
t.right(90)
t.forward(40)
t.left(90)
t.forward(70)
t.left(90)
t.forward(40)
t.right(90)
t.forward(40)
t.left(90)
t.forward(30)

t.end_fill()
t.up()
t.right(90)
t.right(180)
t.forward(40)
t.color(0,0,0)
t.down()

t.begin_fill()
t.right(90)
t.forward(15)
t.forward(15)
t.left(90)
t.circle(15)
t.end_fill()

t.up()
t.forward(70)
t.begin_fill()
t.circle(15)
t.end_fill()

t.up()
t.forward(50)
