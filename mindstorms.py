import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("pink")
    brad.speed(2)

    total_turns = 4
    turn_count = 0

    while (turn_count < total_turns):
        brad.forward(100)
        brad.right(90)
        turn_count = turn_count + 1

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)

def draw_triangle():
    zelda = turtle.Turtle()
    zelda.shape("turtle")
    zelda.color("blue")

    total_turns = 3
    turn_count = 0
    while (turn_count < total_turns):
        zelda.forward(100)
        zelda.right(120)
        turn_count = turn_count + 1
    
draw_square()
draw_circle()
draw_triangle()
