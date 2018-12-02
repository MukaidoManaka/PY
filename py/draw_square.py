import turtle
 
def draw_square():
    window = turtle.Screen()
    window.bgcolor("#6cf")
 
    brad = turtle.Turtle()
    num  = 0
    while num < 4:
          brad.forward(100)
          brad.right(90)
          num += 1
    window.exitonclick()
 
draw_square()