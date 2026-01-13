from asciiArt import asciiMenus
from asciiArt import asciiHelpers
import inventory

# menu constants
MENUDIR = "xDir"
nextGameState = ("regularPlay", "shop", "mainMenu")
MENUMAX = len(nextGameState) - 1
MENUMIN = 0


# main() -> str
# purpose: runs the regular play menu loop, and returns the next game state
#          based on what was chosen
def main():
    # get coins
    coins = inventory.coins

    # return the next game state based on the menu loop
    return asciiHelpers.menuLoop(
        MENUMIN,
        MENUDIR,
        (MENUMIN, MENUMAX),
        # https://www.w3schools.com/python/python_lambda.asp 
        lambda: asciiMenus.getPlayMenuArt(coins),
        nextGameState
    )
