import os
import random

def clamp(num, minNum, maxNum):
    if num < minNum:
        return minNum
    if num > maxNum:
        return maxNum
    return num

# change and clamp
def changeWithClamp(num, change, minNum, maxNum):
    return clamp(num + change, minNum, maxNum)

# clear the terminal
def clearTerminal():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        os.system('cls')
    else:
        # Command for Linux and macOS
        os.system('clear')

# roll dice
def diceRoll(times,size):
    roll = 0
    if size > 0:
        for i in range(times):
            roll += random.randint(1,size)
    else:
        for i in range(times):
            roll += random.randint(size,-1)
    return roll

def changeWithInput(currentSelected, userInput, menuDir, menuMin, menuMax):
    # with input add selected with clamp
    return changeWithClamp(currentSelected, userInput[menuDir], menuMin, menuMax)