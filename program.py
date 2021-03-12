import turtle
import random

widthOfSquare = 120
cordinatesList = [(-250, -230), (-130, -230), (-10, -230), (110, -230), (230, -230),
                  (230, -110), (110, -110), (-10, -110), (-130, -110), (-250, -110),
                  (-250, 10), (-130, 10), (-10, 10), (110, 10), (230, 10),
                  (230, 130), (110, 130), (-10, 130), (-130, 130), (-250, 130),
                  (-250, 250), (-130, 250), (-10, 250), (110, 250), (230, 250),]

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

    t4 = turtle.Turtle()
    t4.shape("snake.gif")
    t4.penup()
    t4.goto(120, 120)

    t5 = turtle.Turtle()
    t5.shape("snake2.gif")
    t5.penup()
    t5.goto(0, -170)

    t6 = turtle.Turtle()
    t6.shape("snake3.gif")
    t6.penup()
    t6.goto(-240, -50)

def setCowAndBull(cow, bull):
    cow.penup()
    cow.goto(-250, -230)

    bull.penup()
    bull.goto(-250, -270)
    
def moveCow(cow, cordinates):
    cow.goto(cordinates[0], cordinates[1])

def moveBull(bull, cordinates):
    bull.goto(cordinates[0], cordinates[1]-40)
    
def startGame():
    cowIndex = 1
    bullIndex = 1

    print('New Game!\n')

    while(True):
        dummy = input('Big Bad Bull: Press Enter to roll dice')
        bullDiceValue = random.randint(1, 6)
        if(bullIndex <= 5 and bullIndex+bullDiceValue >= 6):
            moveBull(bull, cordinatesList[4])
            moveBull(bull, cordinatesList[5])
        elif(bullIndex <= 10 and bullIndex+bullDiceValue >= 11):
            moveBull(bull, cordinatesList[9])
            moveBull(bull, cordinatesList[10])
        elif(bullIndex <= 15 and bullIndex+bullDiceValue >= 16):
            moveBull(bull, cordinatesList[14])
            moveBull(bull, cordinatesList[15])
        elif(bullIndex <= 20 and bullIndex+bullDiceValue >= 21):
            moveBull(bull, cordinatesList[19])
            moveBull(bull, cordinatesList[20])

        bullIndex += bullDiceValue

        if(bullIndex > 25):
            bullIndex = 25
        print(f'You are on square {bullIndex}\n')
        moveBull(bull, cordinatesList[bullIndex-1])

        if (bullIndex >= 25):
            print('bull wins')
            return
        # ------------------
        dummy = input('Fluffy Cow: Press Enter to roll dice')
        cowDiceValue = random.randint(1, 6)
        if(cowIndex <= 5 and cowIndex+cowDiceValue >= 6):
            moveCow(cow, cordinatesList[4])
            moveCow(cow, cordinatesList[5])
        elif(cowIndex <= 10 and cowIndex+cowDiceValue >= 11):
            moveCow(cow, cordinatesList[9])
            moveCow(cow, cordinatesList[10])
        elif(cowIndex <= 15 and cowIndex+cowDiceValue >= 16):
            moveCow(cow, cordinatesList[14])
            moveCow(cow, cordinatesList[15])
        elif(cowIndex <= 20 and cowIndex+cowDiceValue >= 21):
            moveCow(cow, cordinatesList[19])
            moveCow(cow, cordinatesList[20])

        cowIndex += cowDiceValue

        if(cowIndex > 25):
            cowIndex = 25
        moveCow(cow, cordinatesList[cowIndex-1])
        print(f'You are on square {cowIndex}\n')

        if(cowIndex >= 25):
            print('Cow Wins')
            return

if __name__ == '__main__':

    # turtle.getscreen() # gives center turtle
    turtle.title('Python Turtle Graphics')
    turtle.setup(700, 700, 0, 0)
    turtle.addshape("ladder.gif")
    turtle.addshape("ladder2.gif")
    turtle.addshape("ladder3.gif")
    turtle.addshape("snake.gif")
    turtle.addshape("snake2.gif")
    turtle.addshape("snake3.gif")
    turtle.addshape("bull.gif")
    turtle.addshape("cow.gif")


    setupGrid()
    boxNumbers()
    # setImages()

    cow = turtle.Turtle()
    cow.shape("cow.gif")
    
    bull = turtle.Turtle()
    bull.shape("bull.gif")

    setCowAndBull(cow, bull)

    startGame()

    
    turtle.exitonclick()