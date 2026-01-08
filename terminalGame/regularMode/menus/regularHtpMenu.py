from asciiArt import asciiMenus
from asciiArt import asciiHelpers
import userInput
import helperFuncs

MENU_MAX = 1
MENU_MIN = 0
MENU_DIR = "xDir"
HTP_BLOCK_HEIGHT = 16
nextGameState = ("quit")

def main():
    # reset current selected
    currentSelected = MENU_MAX
    # print when first entered
    helperFuncs.clearTerminal()
    print(asciiMenus.getHtpArt()[MENU_MAX])
    while True:
        # get input and use it to change selected
        inputList = userInput.getInputList()
        currentSelected = helperFuncs.changeWithInput(currentSelected, inputList, MENU_DIR, MENU_MIN, MENU_MAX)

        # if space pressed return selected
        if inputList["space"]:
            return nextGameState[currentSelected]

        # clear and update
        helperFuncs.clearTerminal()
        print("no how to play yet")
