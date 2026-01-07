import launchMode
import os
import helperFuncs
from regularMode.menus import regularMainMenu
from regularMode.menus import regularHtpMenu

# set each game state
def setGameStateCompatibility(gameState):
    return "quit"

# set game state
def setGameStateRegular(gameState):
    match gameState:
        case "mainMenu":
            return regularMainMenu.main()
        case "htp":
            return regularHtpMenu.main()
    return "quit"

def main():
    gameState = "mainMenu"

    # clear before starting
    helperFuncs.clearTerminal()

    # get launch mode and start game after
    isRegularMode = launchMode.main()

    while gameState != "quit":
        if isRegularMode:
            gameState = setGameStateRegular(gameState)
        else:
            gameState = setGameStateCompatibility(gameState)

main()