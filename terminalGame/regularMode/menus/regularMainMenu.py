from asciiArt import asciiMenus
from asciiArt import asciiHelpers
import helperFuncs

# menu constants
MENU_DIR = "yDir"
nextGameState = ("quit", "credits", "htp", "playMenu")
MENU_MAX = len(nextGameState) - 1
MENU_MIN = 0

# main() -> str
# purpose: runs the regular main menu loop, and returns the next game state
#          based on what was chosen
def main():
    # returns the next game state
    return asciiHelpers.menuLoop(
        MENU_MAX,
        MENU_DIR,
        (MENU_MIN, MENU_MAX),
        asciiMenus.getMainMenuArt,
        nextGameState
    )