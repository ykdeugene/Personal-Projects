# import Colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
import turtle


def random_color_generator():
    """
    generates a random color from color_list
    :return:
    """
    import random
    color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
                  (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
                  (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
                  (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190),
                  (40, 72, 82), (46, 73, 62), (47, 66, 82)]
    return random.choice(color_list)


def print_dot():
    timmy.dot(20, random_color_generator())


def print_row():
    for row in range(no_of_row):
        print_dot()
        timmy.forward(50)


from turtle import Turtle, Screen


timmy = Turtle()
timmy.speed("fastest")
turtle.colormode(255)  # why does 'timmy.colormode(255)' does not work?

no_of_row = 10
no_of_col = 10

timmy.penup()
timmy.hideturtle()
timmy.goto(-250, -250)

for col in range(no_of_col):
    print_row()
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)
    timmy.backward(500)

screen = Screen()
screen.exitonclick()
