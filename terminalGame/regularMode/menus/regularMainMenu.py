from asciiArt import asciiMenus
import userInput
import helperFuncs


MENU_DIR = "yDir"
nextGameState = ("quit", "credits", "htp", "playMenu")
MENU_MAX = len(nextGameState) - 1
MENU_MIN = 0


def main():
    return helperFuncs.menuLoop(
        MENU_MAX,
        MENU_DIR,
        (MENU_MIN, MENU_MAX),
        asciiMenus.getMainMenuArt,
        nextGameState
    )