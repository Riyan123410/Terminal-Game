import launchMode
import os
import helperFuncs
import userInput
from regularMode.menus import regularMainMenu
from regularMode.menus import regularHtpMenu
from regularMode.menus import regularPlayMenu

coins = 0

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
        case "playMenu":
            return regularPlayMenu.main(coins)
    return "quit"

def main():
    gameState = "mainMenu"

    # clear before starting
    helperFuncs.clearTerminal()

    # TODO: uncomment
    isRegularMode = launchMode.main()
    # get launch mode and start game after
    # if os.name == "nt":
    #     isRegularMode = launchMode.main()
    # else:
    #     isRegularMode = False

    while gameState != "quit":
        if isRegularMode:
            gameState = setGameStateRegular(gameState)
        else:
            gameState = setGameStateCompatibility(gameState)
    
    helperFuncs.clearTerminal()
    print("quit")

main()