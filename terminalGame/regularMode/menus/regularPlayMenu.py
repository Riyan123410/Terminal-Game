from asciiArt import asciiMenus
from asciiArt import asciiHelpers
import userInput
import helperFuncs

MENU_MAX = 2
MENU_MIN = 0
MENU_DIR = "xDir"
nextGameState = ("play", "shop", "mainMenu")

def main(coins):
    return helperFuncs.menuLoop(
        MENU_MIN,
        MENU_DIR,
        (MENU_MIN, MENU_MAX),
        lambda: asciiMenus.getPlayMenuArt(coins),
        nextGameState
    )
