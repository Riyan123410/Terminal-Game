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
        try:
            # try to set mode
            mode = int(input())
            validInput = True

            if not mode in range(0, 2):
                validInput = False
                print("Not in range")
        except:
            print("Invalid input")
    return mode

def afterLaunchSelected(mode):
    # clear screen and print selected mode
    os.system('clear')
    modeList = ["Regular", "Compatibility"]
    print(f"{modeList[mode]} selected...")

    # wait 1 second and reset
    clearInTime(TEXT_DELAY)

# call launch
def main():
    printLaunch()
    mode = selectMode()
    afterLaunchSelected(mode)
    return mode