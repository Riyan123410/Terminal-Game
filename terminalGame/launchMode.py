import helperFuncs
import time
import userInput
from asciiArt import asciiMenus

# constants
TEXT_DELAY = 1


# clearInTime(int/float) -> None
# purpose: waits for the parameter (seconds) long
#          and than clears the terminal
def clearInTime(seconds):
    time.sleep(seconds)
    helperFuncs.clearTerminal()

# printLaunch() -> None
# purpose: clears the terminal and prints the launch mode text
def printLaunch():
    helperFuncs.clearTerminal()
    print(str(asciiMenus.launchMode))

# selectMode() -> bool
# purpose: asks the user to select a launch mode and
#          checks input until a valid option is chosen
#          retuns true if input is 0, returns false if
#          input is 1
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

# afterLaunchSelected(bool) -> None
# purpose: clears the terminal, displays the selected launch
#          mode, then waits before clearing again, takes in the
#          parameter (isRegularMode) to print to the user what
#          was chosen
def afterLaunchSelected(isRegularMode):
    # clear screen and print selected mode
    helperFuncs.clearTerminal()
    print(f"Compatibility Mode: {not isRegularMode}")

    # wait and reset
    clearInTime(TEXT_DELAY)

# main() -> bool
# purpose: main function that displays the launch menu,
#          gets what mode was selected and starts after launch mode
#          finall returns the mode which can be true for regular
#          or fase for compatability
def main():
    printLaunch()
    mode = selectMode()
    afterLaunchSelected(mode)
    return mode