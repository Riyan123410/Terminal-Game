import helperFuncs
import time
import userInput
from asciiArt import asciiMenus

# constants
TEXT_DELAY = 1


# clear after
def clearInTime(seconds):
    time.sleep(seconds)
    helperFuncs.clearTerminal()

# text for select launch mode
def printLaunch():
    helperFuncs.clearTerminal()
    print(str(asciiMenus.launchMode))

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
    helperFuncs.clearTerminal()
    print(f"Compatibility Mode: {not isRegularMode}")

    # wait and reset
    clearInTime(TEXT_DELAY)

# main call all funcitons
def main():
    printLaunch()
    mode = selectMode()
    afterLaunchSelected(mode)
    return mode