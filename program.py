import turtle # import turtle graphics
import random # import random for generating random numbers

"""
Basic Game Development in Python
---------------------------------
This is a Snakes and Ladders game that allows two players to
participate in turns. 

Developed by: ____
Date Created: 13/03/2021

"""

"""
Note: 

Developed using: Ubuntu 20.04, Python 3.8.5
Tested using: Windows 10(version 1909), Python 3.8.5

Compile and run: 
    Ubuntu:     python3 program.py
    Windows:    python program.py

"""

# keeping these unchanged variables as global for easyness
widthOfSquare = 120 
# hardcoded cordinates for the cow and bull, each tuple contains x, y cordinates values 
# for all the 25 squares
cordinatesList = [(-250, -230), (-130, -230), (-10, -230), (110, -230), (230, -230),
                  (230, -110), (110, -110), (-10, -110), (-130, -110), (-250, -110),
                  (-250, 10), (-130, 10), (-10, 10), (110, 10), (230, 10),
                  (230, 130), (110, 130), (-10, 130), (-130, 130), (-250, 130),
                  (-250, 250), (-130, 250), (-10, 250), (110, 250), (230, 250),]

def setupGrid():
    """ Function for setting up grid layout """
    t = turtle.Turtle(visible=False) 
    
    # changing color, width and speed of line
    t.pen(pencolor="blue", pensize=3, speed=10) 
    t.penup() # move without drawing

    # move to bottom left corner
    t.goto(-5*widthOfSquare/2, -5*widthOfSquare/2)
    t.pendown() # start drawing again

    # below for loops draws the grid lines in the turtle window
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
    """ Function for printing box numbers in the grid window """
    t = turtle.Turtle(visible=False) # hide the turtle pointer
    t.pen(pencolor="red", speed=10) # changing color and speed
    t.penup() # hide the drawings
    
    # this part will print numbers 1 to 5 on the grid
    xCord = -(widthOfSquare*5/2-5)
    for i in range(5):
        t.goto(xCord, -210)
        t.write(str(i+1), font=('', 18, 'italic')) # set the default system font of OS
        xCord += widthOfSquare
    
    # this part will print numbers 6 to 10 on the grid
    t.left(90)
    t.forward(widthOfSquare)
    t.left(90)
    for i in range(6, 11):
        t.write(str(i), font=('', 18, 'italic')) # set the default system font of OS
        t.forward(widthOfSquare) # move to next square
    
    # this part will print numbers 11 to 15 on the grid
    t.right(90)
    t.forward(widthOfSquare)
    t.right(90)
    t.forward(widthOfSquare)
    for i in range(11, 16):
        t.write(str(i), font=('', 18, 'italic')) # set the default system font of OS
        t.forward(widthOfSquare) # move to next square

    # this part will print numbers 16 to 20 on the grid
    t.left(90)
    t.forward(widthOfSquare)
    t.left(90)
    t.forward(widthOfSquare)
    for i in range(16, 21):
        t.write(str(i), font=('', 18, 'italic')) # set the default system font of OS
        t.forward(widthOfSquare) # move to next square

    # this part will print numbers 21 to 25 on the grid
    t.right(90)
    t.forward(widthOfSquare)
    t.right(90)
    t.forward(widthOfSquare)
    for i in range(21, 26):
        t.write(str(i), font=('', 18, 'italic')) # set the default system font of OS
        t.forward(widthOfSquare) # move to next square

def setImages():
    """ Function for setting up ladders and snakes on the game window """

    # ladder of squares 9-12
    t1 = turtle.Turtle()
    t1.shape("ladder.gif") # add the image to turtle pointer
    t1.penup() # hide the moving path
    t1.goto(-100, -50) # postion in the correct place

    # ladder of squares 18-23
    t2 = turtle.Turtle()
    t2.shape("ladder2.gif") # add the image to turtle pointer
    t2.penup() # hide the moving path
    t2.goto(0, 190)

    # ladder of squares 5-15
    t3 = turtle.Turtle()
    t3.shape("ladder3.gif") # add the image to turtle pointer
    t3.penup() # hide the moving path
    t3.goto(250, -140)

    # snake of squares 14-24
    t4 = turtle.Turtle()
    t4.shape("snake.gif") # add the image to turtle pointer
    t4.penup() # hide the moving path
    t4.goto(120, 120)

    # snake of squares 3-8
    t5 = turtle.Turtle()
    t5.shape("snake2.gif") # add the image to turtle pointer
    t5.penup() # hide the moving path
    t5.goto(0, -170)

    # snake of squares 1-20
    t6 = turtle.Turtle()
    t6.shape("snake3.gif") # add the image to turtle pointer
    t6.penup() # hide the moving path
    t6.goto(-240, -50)

def setCowAndBull(cow, bull):
    """ Function for setting up cow and bull in the initial position """
    
    cow.penup() # hide the moving path
    cow.goto(-250, -230) # position in the correct place

    bull.penup() # hide the moving path
    bull.goto(-250, -270) # position in the correct place
    
def moveCow(cow, cordinates):
    """ 
    Function for moving the cow to given cordinates. 
    cordinates are passed as a tuple of (x, y)
    cow object is also passed as a parameter
    """
    cow.goto(cordinates[0], cordinates[1])

def moveBull(bull, cordinates):
    """ 
    Function for moving the bull to given cordinates. 
    cordinates are passed as a tuple of (x, y)
    """

    # the bull is positioned 40 units below the cow
    # along y axis
    bull.goto(cordinates[0], cordinates[1]-40)
    
def startGame():
    """ 
    Function for keep the game running until user interrupts by keyboard
    """

    # keeping track of the squares of cow and bull
    # intially they are at 1st square
    cowIndex = 1
    bullIndex = 1

    print('New Game!\n')
    
    # keep prompting user to press enter
    while(True):
        # get the Enter press to dummy variable
        dummy = input('Big Bad Bull: Press Enter to roll dice')
        
        # generating a random value between 1-6 for the bull
        bullDiceValue = random.randint(1, 6)
        print(f'bull dice value: {bullDiceValue}') # printing the dice value
        
        # logic for moving between corner squares
        if(bullIndex < 5 and bullIndex+bullDiceValue >= 6):
            moveBull(bull, cordinatesList[4])
            moveBull(bull, cordinatesList[5])
        if(bullIndex <= 10 and bullIndex+bullDiceValue >= 11):
            moveBull(bull, cordinatesList[9])
            moveBull(bull, cordinatesList[10])
        if(bullIndex <= 15 and bullIndex+bullDiceValue >= 16):
            moveBull(bull, cordinatesList[14])
            moveBull(bull, cordinatesList[15])
        if(bullIndex <= 20 and bullIndex+bullDiceValue >= 21):
            moveBull(bull, cordinatesList[19])
            moveBull(bull, cordinatesList[20])
        
        # update the square value of bull
        bullIndex += bullDiceValue

        # reset suquare value to 25 if it is larger
        if(bullIndex > 25):
            bullIndex = 25
        
        # move the bull to correct position
        moveBull(bull, cordinatesList[bullIndex-1])
        
        # logic for checking stairs and snakes
        if(bullIndex == 5): # stairs
            moveBull(bull, cordinatesList[14])
            bullIndex = 15
        elif(bullIndex == 9):
            moveBull(bull, cordinatesList[11])
            bullIndex = 12
        elif(bullIndex == 18):
            moveBull(bull, cordinatesList[22])
            bullIndex = 23
        elif(bullIndex == 8): # snakes
            moveBull(bull, cordinatesList[2])
            bullIndex = 3
        elif(bullIndex == 20):
            moveBull(bull, cordinatesList[0])
            bullIndex = 1
        elif(bullIndex == 24):
            moveBull(bull, cordinatesList[13])
            bullIndex = 14

        print(f'You are on square {bullIndex}\n')

        # check if bull has come to the end
        if (bullIndex == 25):
            print('Bull Wins')
            turtle.clearscreen() # clear everything in window
            turtle.bgpic("win.gif") # show win image
            turtle.update()
            dummy = input('Press Enter to start new game') # wait to press Enter
            turtle.clearscreen() # clear win image
            return # return to main function
        
        # ------------------
        # getting user input for cow and store in a dummy variable
        dummy = input('Fluffy Cow: Press Enter to roll dice')
        # generating dice value for cow
        cowDiceValue = random.randint(1, 6)
        # printing dice value
        print(f'cow dice value: {cowDiceValue}')

        # logic for move between corner squares
        if(cowIndex < 5 and cowIndex+cowDiceValue >= 6):
            moveCow(cow, cordinatesList[4])
            moveCow(cow, cordinatesList[5])
        if(cowIndex <= 10 and cowIndex+cowDiceValue >= 11):
            moveCow(cow, cordinatesList[9])
            moveCow(cow, cordinatesList[10])
        if(cowIndex <= 15 and cowIndex+cowDiceValue >= 16):
            moveCow(cow, cordinatesList[14])
            moveCow(cow, cordinatesList[15])
        if(cowIndex <= 20 and cowIndex+cowDiceValue >= 21):
            moveCow(cow, cordinatesList[19])
            moveCow(cow, cordinatesList[20])

        # update the square value of cow
        cowIndex += cowDiceValue

        # if index is larger than 25, reset it to 25
        if(cowIndex > 25):
            cowIndex = 25
        
        # move the cow to correct position
        moveCow(cow, cordinatesList[cowIndex-1])

        # logic for checking stairs and snakes
        if(cowIndex == 5): # stairs
            moveCow(cow, cordinatesList[14])
            cowIndex = 15
        elif(cowIndex == 9):
            moveCow(cow, cordinatesList[11])
            cowIndex = 12
        elif(cowIndex == 18):
            moveCow(cow, cordinatesList[22])
            cowIndex = 23
        elif(cowIndex == 8): # snakes
            moveCow(cow, cordinatesList[2])
            cowIndex = 3
        elif(cowIndex == 20):
            moveCow(cow, cordinatesList[0])
            cowIndex = 1
        elif(cowIndex == 24):
            moveCow(cow, cordinatesList[13])
            cowIndex = 14

        print(f'You are on square {cowIndex}\n')

        # check if cow has come to end
        if(cowIndex == 25):
            print('Cow Wins')
            turtle.clearscreen() # clear everything
            turtle.bgpic("win.gif") # show win image
            turtle.update()
            dummy = input('Press Enter to start new game') # wait to press Enter
            turtle.clearscreen() # clear win image
            return # return to main function

if __name__ == '__main__':
    
    turtle.title('Python Turtle Graphics') # set title of window
    turtle.setup(700, 700, 0, 0) # this is a 700 x 700 window with starting position (0,0)

    # adding .gif images to program
    turtle.addshape("ladder.gif")
    turtle.addshape("ladder2.gif")
    turtle.addshape("ladder3.gif")
    turtle.addshape("snake.gif")
    turtle.addshape("snake2.gif")
    turtle.addshape("snake3.gif")
    turtle.addshape("bull.gif")
    turtle.addshape("cow.gif")
    turtle.addshape("win.gif")

    # the game runs infinitely until user interrupts by keyboard
    while(True):
        setupGrid() # painting box
        boxNumbers() # painting box numbers
        setImages() # adding images
        
        # creating cow figure
        cow = turtle.Turtle()
        cow.shape("cow.gif")
        
        # creating bull figure
        bull = turtle.Turtle()
        bull.shape("bull.gif")

        # move cow and bull to intial positions
        setCowAndBull(cow, bull)
        startGame() # run the game


    turtle.exitonclick() # keep the window until user terminates

