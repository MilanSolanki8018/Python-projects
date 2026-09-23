import random
import turtle as t
# import colorgram

"""
rgb_list = []
colors = colorgram.extract('color.jpeg',30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_list.append(new_color)

print(rgb_list)
"""


timy = t.Turtle()
rgb_list = [(224, 227, 234), (242, 236, 215), (226, 241, 233), (241, 229, 238), (182, 166, 129), (147, 163, 183), (122, 98, 69), (13, 22, 47), (75, 98, 124), (47, 25, 14), (209, 205, 144), (175, 151, 165), (149, 172, 157), (47, 15, 27), (117, 84, 100), (79, 107, 87), (154, 146, 75), (16, 33, 21), (182, 185, 214), (41, 55, 105), (112, 120, 158), (176, 202, 187), (209, 180, 194), (152, 112, 133), (97, 43, 59), (107, 142, 117), (80, 76, 31), (39, 79, 56), (102, 45, 36), (218, 180, 172)]
t.colormode(255)
timy.speed(50)
timy.penup()
timy.hideturtle()
timy.setheading(225)
timy.forward(300)
timy.setheading(0)
numbers_of_dots = 100

for dot in range(1,numbers_of_dots+1):
    timy.dot(20, random.choice(rgb_list))
    timy.forward(50)

    if dot % 10 == 0:
        timy.setheading(90)
        timy.forward(50)
        timy.setheading(180)
        timy.forward(500)
        timy.setheading(0)


screen = t.Screen()
screen.exitonclick()
