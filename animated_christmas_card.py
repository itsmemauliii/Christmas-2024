import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("sky blue")
screen.title("Merry Christmas")

# Create a turtle for drawing the tree
tree = turtle.Turtle()
tree.color("green")
tree.width(5)

# Function to draw a triangle for the tree
def draw_triangle(size, color):
    tree.fillcolor(color)
    tree.begin_fill()
    for _ in range(3):
        tree.forward(size)
        tree.left(120)
    tree.end_fill()

# Function to draw a square for the tree trunk
def draw_trunk():
    tree.color("brown")
    tree.begin_fill()
    for _ in range(4):
        tree.forward(40)
        tree.left(90)
    tree.end_fill()

# Function to draw ornaments
def draw_ornaments():
    tree.penup()
    tree.goto(-50, 100)
    tree.dot(20, "red")
    tree.goto(30, 130)
    tree.dot(20, "yellow")
    tree.goto(-20, 60)
    tree.dot(20, "blue")
    tree.goto(10, 80)
    tree.dot(20, "purple")

# Draw the tree
tree.penup()
tree.goto(-100, -100)
tree.pendown()
draw_triangle(200, "green")
tree.penup()
tree.goto(-70, -50)
tree.pendown()
draw_triangle(150, "green")
tree.penup()
tree.goto(-40, 0)
tree.pendown()
draw_triangle(100, "green")

# Draw the trunk
tree.penup()
tree.goto(-20, -100)
tree.pendown()
draw_trunk()

# Draw ornaments on the tree
draw_ornaments()

# Draw the star on top of the tree
tree.penup()
tree.goto(-10, 140)
tree.pendown()
tree.color("yellow")
tree.begin_fill()
for _ in range(5):
    tree.forward(30)
    tree.right(144)
tree.end_fill()

# Add a message to the card
tree.penup()
tree.goto(-150, -200)
tree.pendown()
tree.color("red")
tree.write("Merry Christmas!", font=("Arial", 24, "bold"))

# Hide the turtle and display the card
tree.hideturtle()

# Keep the window open
turtle.done()
