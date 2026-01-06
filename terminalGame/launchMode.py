import os
import time
import Input

# constants
TEXT_DELAY = 1


# clear after
def clearInTime(seconds):
    time.sleep(seconds)
    os.system('clear')

# text for select launch mode
def printLaunch():
    os.system('clear')
    print("Please full screen your terminal in order for ascii art to display properly, \nif art is not displayed correctly compatibilty mode can be used")
    print("Choose by enterying the corresponding number in the terminal: ")
    print("\n> Continue[0] - ASCII art, input uses WASD and SPACE\n> Compatibility Mode[1] - No ASCII art, input uses characters entered in terminal(for non windows users)")

# select launch mode
def selectMode():
    # set input to invalid
    validInput = False
    # loop until a valid launch mode is selected
    while not validInput:
        # try to set mode as if input is not a number there will be an error
        try:
            # input is true until it is proven false
            validInput = True
            currentInput = int(input())
            # based on input check if its the regular mode
            match currentInput:
                case 0: 
                    isRegularMode = True
                case 1: 
                    isRegularMode = False
                case _:
                    validInput = False
                    print("Not in range")
        except:
            validInput = False
            print("Invalid input")
    return isRegularMode

def afterLaunchSelected(isRegularMode):
    # clear screen and print selected mode
    os.system('clear')
    print(f"Compatibility Mode: {not isRegularMode}")

    # wait and reset
    clearInTime(TEXT_DELAY)

# main call all funcitons
def main():
    printLaunch()
    mode = selectMode()
    afterLaunchSelected(mode)
    return mode