from turtle import Turtle,Screen
from random import random


class A:
    print("OOP")

obj = A()

welly = Turtle()
print(welly)
welly.shape("turtle")
welly.color("red")
welly.forward(100)
welly.back(100)
welly.left(250)
welly.back(150)
welly.home()
welly.forward(100)

# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     welly.right(angle)
#     welly.fd(steps)

my_screen = Screen()
print(my_screen)
my_screen.exitonclick()



