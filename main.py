import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()

#turtle.colormode(255)


# generating random color
def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors_tuple = (r, g, b)
    return colors_tuple


# generating spot painting
def spot_painting_generator(painting_size):
    size_of_dots = 8
    gap_between_dots = size_of_dots*5

    my_turtle.goto(-25 * painting_size, -25 * painting_size)
    for i in range(painting_size):
        for j in range(painting_size):
            my_turtle.dot(size_of_dots, random_color_generator())
            my_turtle.forward(gap_between_dots)
        my_turtle.goto((-25 * painting_size), (my_turtle.ycor() + gap_between_dots))


painting_size_input = int(input("Preferred painting size: "))

spot_painting_generator(painting_size_input)

turtle.Screen().exitonclick()