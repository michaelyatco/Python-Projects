import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range (1,4):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_rhombus(some_turtle):
    for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.left(45)
        some_turtle.forward(100)
        some_turtle.left(135)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad - Draws a square
    #brad = turtle.Turtle()
    #brad.shape("turtle")
    #brad.color("yellow")
    #brad.speed(7)
    #for i in range (1,37):
        #draw_square(brad)
        #brad.right(10)
    #Create the turtle Angie - Draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(30)
    for i in range (1,120):
        draw_triangle(angie)
        angie.right(3)

    angie.setposition(0,-200)

    lucius = turtle.Turtle()
    lucius.shape("turtle")
    lucius.color("pink")
    lucius.speed(30)
    for i in range (1,37):
        draw_rhombus(lucius)
        lucius.right(10)

    window.exitonclick()
    
draw_art()
