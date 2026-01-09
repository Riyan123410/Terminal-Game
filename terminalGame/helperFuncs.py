import os
import random
import userInput


# clamp(int/float, int/float, int/float) -> int/float
# purpose: sets the paramater (maxNum) to be at least the entered input (minNum)
#          and at most the parameter (maxNum)
# examples:
#          clamp(5, 0, 10) -> 5
#          clamp(-5.6, -2.1, 10) -> -2.1
#          clamp(0, 0, 0) -> 0
def clamp(num, minNum, maxNum):
    if num < minNum:
        return minNum
    if num > maxNum:
        return maxNum
    return num

# changeWithClamp(int/float, int/float, int/float, int/float) -> int/float
# purpose: takes in the number (num) adding the parameter (change) it than
#          clamps this number to be withen (minNum) and (maxNum)
# examples:
#          changeWithClamp(5, 3, 0, 10) -> 8
#          changeWithClamp(5, -10, 0, 10) -> 0
#          changeWithClamp(5.5, 10, 0, 10.5) -> 10.5
def changeWithClamp(num, change, minNum, maxNum):
    return clamp(num + change, minNum, maxNum)

# clearTerminal() -> None
# purpose: Clears the terminal based on the current operating system
def clearTerminal():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        os.system('cls')
    else:
        # Command for Linux and macOS
        os.system('clear')


# diceRoll(int, int) -> int
# purpose: returns the sum of a random number from 1 to the input (size)
#          the number of numbers generated are based on the parameter (times)
# examples:
#          diceRoll(2, 6) -> 2 to 12
#          diceRoll(3, 1) -> 3
#          diceRoll(1, -3) -> -1 to -3
def diceRoll(times,size):
    roll = 0
    if size > 0:
        for i in range(times):
            roll += random.randint(1,size)
    else:
        for i in range(times):
            roll += random.randint(size,-1)
    return roll

# testing not plausible due to random


# menuLoop(int, dict, str, (), function) -> str
# purpose: The menu loop that handles input, selection, ASCII art display,
#          and returns the next game state. To do this it needs the starting
#          selecting with (currentSelected), the direction the menu is going
#          in (menuDir) can be "xDir" or "yDir" making it accept WS or AD input, 
#          the range (menuRange) of the optns and (nextStates) for a list of 
#          all possible game states the menu can lead to in order
# examples:
#          menuLoop(2, "yDir", (0, 2), getMainMenuArt, ("play", "shop", "mainMenu")) -> "mainMenu"
#          menuLoop(0, "xDir", (0, 3), getPlayMenuArt, ("quit", "credits", "htp", "playMenu")) -> "quit"
def menuLoop(currentSelected, menuDir, menuRange, artFunc, nextStates):

    # reset terminal and try to print art function
    clearTerminal()
    try:
        print(artFunc()[currentSelected])
    except:
        print("art function is incorrect")
    
    while True:
        # try to change menu
        inputList = userInput.getInputList()
        try:
            currentSelected = changeWithClamp(currentSelected, inputList[menuDir], menuRange[0], menuRange[1])
        except:
            print("user input is incorrect")
        
        # if selected return next state
        if inputList["space"]:
            return nextStates[currentSelected]
        
        # try to update menu
        clearTerminal()
        try:
            print(artFunc()[currentSelected])
        except:
            print("function for ascii art is out of range")

# getCoins() -> int
# purpose: returns the number of coins saved in the file save.txt
def getCoins():
    saveFile = open("save.txt", "r")
    return int(saveFile.readline())