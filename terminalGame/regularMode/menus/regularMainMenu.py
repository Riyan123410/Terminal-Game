from asciiArt import asciiMenus
import Input
import helperFuncs

MENU_MAX = 2
MENU_MIN = 0
MENU_DIR = "vertical"
nextGameState = ("quit","htp", "play")

def main():
    # reset current selected
    currentSelected = MENU_MAX
    # print when first entered
    helperFuncs.clearTerminal()
    print(asciiMenus.getMainMenuArt()[MENU_MAX])
    while True:
        # get input and use it to change selected
        inputList = Input.getInputList()
        currentSelected = helperFuncs.changeWithInput(currentSelected, inputList, MENU_DIR, MENU_MIN, MENU_MAX)

        # if space pressed return selected
        if inputList[2] == 1:
            return nextGameState[currentSelected]

        # clear and update
        helperFuncs.clearTerminal()
        print(asciiMenus.getMainMenuArt()[currentSelected])
