import random
# from turtle import Turtle,Screen
import turtle as t

#1. create squer
"""
welly = Turtle()
welly.color("green")
welly.shape("turtle")
welly.right(90)
welly.forward(100)
welly.right(90)
welly.forward(100)
welly.right(90)
welly.forward(100)
welly.right(90)
welly.forward(100)
# welly.home() 
"""

# create dashed line
"""
dashed = Turtle()

for _ in range(15):
    dashed.forward(10)
    dashed.penup()
    # dashed.color("white")
    dashed.forward(10)
    dashed.pendown()
    # dashed.color("black")

dashed.color("red")
"""

#genrate traingle,squre and other
"""
color = ['light salmon','indigo','gold','dark turquoise','blue','green','grey']
math = Turtle()
def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        math.forward(100)
        math.right(angle)

for shape in range(3,9):
   math.color(random.choice(color))
   draw_shape(shape)

"""

# random walk
"""
walk = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
# color = ['light salmon','indigo','gold','dark turquoise','blue','green','grey']
step = [0,90,180,270]
walk.pensize(10)
walk.speed(10)
for _ in range(50):
    walk.forward(30)
    walk.setheading(random.choice(step))
    walk.color(random_color())
    
"""

#create a spirograph
spiro = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
spiro.speed(100)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        spiro.color(random_color())
        spiro.circle(150)
        spiro.setheading(spiro.heading() + size_of_gap)

draw_spirograph(5)







display = t.Screen()
display.exitonclick()