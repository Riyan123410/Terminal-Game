from asciiArt import asciiMenus
from asciiArt import asciiHelpers
import userInput
import helperFuncs

MENU_MAX = 1
MENU_MIN = 0
MENU_DIR = "xDir"
nextGameState = ("play", "shop")

def main(coins):
    # reset current selected
    currentSelected = MENU_MIN
    # print when first entered
    helperFuncs.clearTerminal()
    print(asciiMenus.getPlayMenuArt(coins)[currentSelected])
    while True:
        # get input and use it to change selected
        inputList = userInput.getInputList()
        currentSelected = helperFuncs.changeWithInput(currentSelected, inputList, MENU_DIR, MENU_MIN, MENU_MAX)

        # if space pressed return selected
        if inputList["space"]:
            return nextGameState[currentSelected]

        # clear and update
        helperFuncs.clearTerminal()
        print(asciiMenus.getPlayMenuArt(coins)[currentSelected])
