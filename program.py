import turtle

widthOfSquare = 120
def setupGrid():
    t = turtle.Turtle(visible=False)
    t.pen(pencolor="blue", pensize=3, speed=10)
    t.penup()
    t.goto(-5*widthOfSquare/2, -5*widthOfSquare/2)
    t.pendown()
    for _ in range(4):
        t.forward(5*widthOfSquare)
        t.left(90)
    
    for y in range(int(-1.5*widthOfSquare), int(1.5*widthOfSquare)+1, widthOfSquare): 
        t.penup()
        t.goto(-5*widthOfSquare/2, y)
        t.pendown()
        t.forward(5*widthOfSquare)
    t.right(90)
    for x in range(int(-1.5*widthOfSquare), int(1.5*widthOfSquare+1), widthOfSquare): 
        t.penup()
        t.goto(x, 5*widthOfSquare/2)
        t.pendown()
        t.forward(5*widthOfSquare)
    
def boxNumbers():
    t = turtle.Turtle(visible=False)
    t.pen(pencolor="red", speed=10)
    t.penup()
    xCord = -(widthOfSquare*5/2-5)
    for i in range(5):
        t.goto(xCord, -210)
        t.write(str(i+1), font=('', 18, 'italic')) # set the default system font, check this on windows 10
        xCord += widthOfSquare
    
    t.left(90)
    t.forward(widthOfSquare)
    t.left(90)
    for i in range(6, 11):
        t.write(str(i), font=('', 18, 'italic')) # set the default system font, check this on windows 10
        t.forward(widthOfSquare)
    
    t.right(90)
    t.forward(widthOfSquare)
    t.right(90)
    t.forward(widthOfSquare)
    for i in range(11, 16):
        t.write(str(i), font=('', 18, 'italic')) # set the default system font, check this on windows 10
        t.forward(widthOfSquare)

    t.left(90)
    t.forward(widthOfSquare)
    t.left(90)
    t.forward(widthOfSquare)
    for i in range(16, 21):
        t.write(str(i), font=('', 18, 'italic')) # set the default system font, check this on windows 10
        t.forward(widthOfSquare)

    t.right(90)
    t.forward(widthOfSquare)
    t.right(90)
    t.forward(widthOfSquare)
    for i in range(21, 26):
        t.write(str(i), font=('', 18, 'italic')) # set the default system font, check this on windows 10
        t.forward(widthOfSquare)

def setImages():
    t1 = turtle.Turtle()
    t1.shape("ladder.gif")
    t1.penup()
    t1.goto(-100, -50)

    t2 = turtle.Turtle()
    t2.shape("ladder2.gif")
    t2.penup()
    t2.goto(0, 190)

    t3 = turtle.Turtle()
    t3.shape("ladder3.gif")
    t3.penup()
    t3.goto(250, -140)

if __name__ == '__main__':

    # turtle.getscreen() # gives center turtle
    turtle.title('Python Turtle Graphics')
    turtle.setup(700, 700, 0, 0)
    turtle.addshape("ladder.gif")
    turtle.addshape("ladder2.gif")
    turtle.addshape("ladder3.gif")

    setupGrid()
    boxNumbers()
    setImages()
    
    
    
    turtle.exitonclick()