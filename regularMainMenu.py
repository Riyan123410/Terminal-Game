from asciiArt import Menus
import Input
import helperFuncs
import os

currentSelected = 1
MENU_MAX = 1
MENU_MIN = 0
gameState = ("how to play", "play")

def main():
    # print when first entered
    print(Menus.getMainMenuArt()[0])
    while True:
        # input
        key = Input.getInputList()
        changeSelectedBy(key[1])
        # if selected return
        if key[2] == 1:
            os.system('clear')
            return gameState[currentSelected]

# change selected
def changeSelectedBy(change):
    # get current selected
    global currentSelected
    # increase, clamp
    currentSelected = helperFuncs.changeWithClamp(currentSelected, change, MENU_MIN, MENU_MAX)

    # update menu
    os.system('clear')
    print(Menus.getMainMenuArt()[currentSelected])