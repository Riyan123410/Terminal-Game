from asciiArt import asciiMenus
import userInput
import helperFuncs

MENU_MAX = 2
MENU_MIN = 0
MENU_DIR = "yDir"
nextGameState = ("quit","htp", "playMenu")



def main():
    return helperFuncs.menuLoop(
        MENU_MAX,
        MENU_DIR,
        (MENU_MIN, MENU_MAX),
        asciiMenus.getMainMenuArt,
        nextGameState
    )