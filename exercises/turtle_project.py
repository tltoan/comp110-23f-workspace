"""TODO: Three pinwheels that has 7 different colors for each blades."""

__author__ = ""
from turtle import Turtle, Screen, colormode, done

colormode(255)
bill: Turtle = Turtle()
screen = Screen()  # import screen color
screen.bgcolor("lightblue")

oval_color = ["red", "blue", "green", "violet", "orange", "indigo", "yellow"]


def draw_stem(t: Turtle, x: float, y: float,) -> None:
    """Get turtle to draw a stem based on parameters."""
    t.color("green")
    t.begin_fill()
    t.fillcolor("brown")
    t.penup()
    t.goto(x, y)
    t.pendown()
    i: int = 0
    while (i < 4):  # Loop to draw the stem shape
        if i % 2 != 0:
            t.forward(215)
            t.left(90)
        else:
            t.forward(25)
            t.left(90)
        i = i + 1
    t.end_fill()
    t.penup()


# Function to draw a circle at given parameters
def draw_circle(ctur: Turtle, x: float, y: float, radius: float,) -> None:
    """Draw a circle at given parameters."""
    ctur.color()
    ctur.speed(0)
    ctur.penup()
    ctur.fillcolor("black")
    ctur.goto(x, y)
    ctur.pendown()
    ctur.begin_fill()
    ctur.circle(radius)
    ctur.end_fill()
    

# Function to draw an oval at given parameters
def draw_oval(tur: Turtle, x: float, y: float, width: float, height: float, targetAngle: int) -> None:
    """Draw an oval at given parameters."""
    tur.penup()
    tur.pencolor("black")
    tur.goto(x, y)
    tur.pendown()
    tur.begin_fill()
    tur.setheading(targetAngle)  # Set the initial drawing angle
    tur.circle(width, 95)
    tur.circle(height, 90)
    tur.end_fill()


# Function to draw pinwheels at specified positions and sizes
def drawPinwheel(x: int, y: int, width: float, height: float,) -> None:
    """Drawing Pinwheels."""
    currentAngle = 0  # Initialize the starting angle for drawing ovals
    for i in range(7):
        bill.color(oval_color[i % len(oval_color)])
        print(oval_color[i % len(oval_color)])
        bill.speed(80)
        bill.penup()
        bill.goto(0, 0)
        draw_oval(bill, x, y, width, height, currentAngle)
        currentAngle += 51
    bill.setheading(0)  # Set the turtle heading angle to 0 (east)
    draw_circle(bill, x, y - 10, 20)
    bill.hideturtle()   


# Main function to draw the background, stems, and pinwheels
def main() -> None:
    """Entrypoint."""
    bill.penup()
    bill.goto(-360, 0)  # Move the turtle to the specified position (-360, 0)
    bill.pendown()
    bill.begin_fill()
    bill.fillcolor(48, 157, 55)   # Set fill color using RGB values
    for _ in range(2):
        bill.forward(720)  # Draw the width of the box
        bill.right(90)  # Turn 90 degrees to draw the height of the box
        bill.forward(360)  # Draw the height of the box
        bill.right(90) 
    bill.end_fill()
    #  Draw stems and pinwheels at specified positions
    draw_stem(bill, -210, -100)
    drawPinwheel(-200, 150, 70, 40)
    draw_stem(bill, 140, -120)
    drawPinwheel(150, 100, 80, 35)
    draw_stem(bill, -102, -340)
    drawPinwheel(-90, -120, 95, 45)


main()  # Main function to draw the background, stems, and pinwheels

done()  # Keep the turtle graphics window open
