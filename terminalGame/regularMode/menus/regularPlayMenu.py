from asciiArt import asciiMenus
from asciiArt import asciiHelpers
import helperFuncs
import inventory

# menu constants
MENU_DIR = "xDir"
nextGameState = ("regularPlay", "shop", "mainMenu")
MENU_MAX = len(nextGameState) - 1
MENU_MIN = 0


# main() -> str
# purpose: runs the regular play menu loop, and returns the next game state
#          based on what was chosen
def main():
    # get coins
    coins = inventory.coins

    # return the next game state based on the menu loop
    return asciiHelpers.menuLoop(
        MENU_MIN,
        MENU_DIR,
        (MENU_MIN, MENU_MAX),
        lambda: asciiMenus.getPlayMenuArt(coins),
        nextGameState
    )
