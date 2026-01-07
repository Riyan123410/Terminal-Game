from asciiArt import asciiMenus
import Input
import helperFuncs

MENU_MAX = 2
MENU_MIN = 0
gameState = ("quit","htp", "play")

def main():
    # reset current selected
    currentSelected = MENU_MAX
    # print when first entered
    print(asciiMenus.getMainMenuArt()[MENU_MAX])
    while True:
        # input
        inputLists = Input.getInputList()
        changeSelectedBy(currentSelected, inputLists[1])
        # if selected return
        if inputLists[2] == 1:
            helperFuncs.clearTerminal()
            return gameState[currentSelected]

# change selected
def changeSelectedBy(currentSelected, change):
    # increase, clamp
    currentSelected = helperFuncs.changeWithClamp(currentSelected, change, MENU_MIN, MENU_MAX)

    # update menu
    helperFuncs.clearTerminal()
    print(asciiMenus.getMainMenuArt()[currentSelected])