import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()

turtle.Screen().setup(width=700, height=700)
turtle.colormode(255)


# generating random color
def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors_tuple = (r, g, b)
    return colors_tuple


# generating spot painting
def spot_painting_generator(painting_size):
    size_of_dots = 15
    gap_between_dots = size_of_dots * 3
    coordinate = -20 * painting_size

    my_turtle.goto(coordinate, coordinate)  # starting point

    for i in range(painting_size):
        for j in range(painting_size):
            my_turtle.dot(size_of_dots, random_color_generator())
            my_turtle.forward(gap_between_dots)

        # to start from a new line after each loop
        my_turtle.goto(coordinate, (my_turtle.ycor() + gap_between_dots))


# painting_size_input = int(input("Preferred painting size: "))
painting_size_input = int(turtle.numinput(title="Spot painting", prompt="Preferred painting size(<=15): ", default=10, minval=1, maxval=15))

spot_painting_generator(painting_size_input)

turtle.Screen().exitonclick()
