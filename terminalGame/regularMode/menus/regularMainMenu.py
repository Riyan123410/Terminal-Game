from asciiArt import asciiMenus
from asciiArt import asciiHelpers
import helperFuncs

# menu constants
MENUDIR = "yDir"
nextGameState = ("quit", "credits", "htp", "playMenu")
MENUMAX = len(nextGameState) - 1
MENUMIN = 0

# main() -> str
# purpose: runs the regular main menu loop, and returns the next game state
#          based on what was chosen
def main():
    # returns the next game state
    return asciiHelpers.menuLoop(
        MENUMAX,
        MENUDIR,
        (MENUMIN, MENUMAX),
        asciiMenus.getMainMenuArt,
        nextGameState
    )