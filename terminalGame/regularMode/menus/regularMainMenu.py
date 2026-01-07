from asciiArt import asciiMenus
import Input
import helperFuncs


currentSelected = 2
MENU_MAX = currentSelected
MENU_MIN = 0
gameState = ("quit","htp", "play")

def main():
    # print when first entered
    print(asciiMenus.getMainMenuArt()[MENU_MAX])
    while True:
        # input
        key = Input.getInputList()
        changeSelectedBy(key[1])
        # if selected return
        if key[2] == 1:
            helperFuncs.clearTerminal()
            return gameState[currentSelected]

# change selected
def changeSelectedBy(change):
    # get current selected
    global currentSelected
    # increase, clamp
    currentSelected = helperFuncs.changeWithClamp(currentSelected, change, MENU_MIN, MENU_MAX)

    # update menu
    helperFuncs.clearTerminal()
    print(asciiMenus.getMainMenuArt()[currentSelected])