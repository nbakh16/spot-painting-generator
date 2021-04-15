import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()

#turtle.colormode(255)

#generating random color
def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors_tuple = (r, g, b)
    return colors_tuple
	
#generating spot painting
def spot_painting_generator(painting_size):
    
    my_turtle.goto(-25 * painting_size, -25 * painting_size)
    for i in range(painting_size):
        for j in range(painting_size):
            my_turtle.dot(20, random_color_generator())
            my_turtle.forward(50)
        my_turtle.goto((-25 * painting_size), (my_turtle.ycor() + 50))


painting_size_input = int(input("Preferred painting size: "))

spot_painting_generator(painting_size_input)


turtle.Screen().exitonclick()