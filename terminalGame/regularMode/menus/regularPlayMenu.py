from asciiArt import asciiMenus
from asciiArt import asciiHelpers
import userInput
import helperFuncs

# menu constants
MENU_DIR = "xDir"
nextGameState = ("play", "shop", "mainMenu")
MENU_MAX = len(nextGameState) - 1
MENU_MIN = 0

def main():
    # get coins
    coins = helperFuncs.getCoins()

    # return the next game state based on the menu loop
    return helperFuncs.menuLoop(
        MENU_MIN,
        MENU_DIR,
        (MENU_MIN, MENU_MAX),
        lambda: asciiMenus.getPlayMenuArt(coins),
        nextGameState
    )
