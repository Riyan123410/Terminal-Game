import launchMode
import os
import helperFuncs
import userInput
from regularMode.menus import regularMainMenu
from regularMode.menus import regularHtpMenu
from regularMode.menus import regularPlayMenu

coins = 0

# setGameStateCompatibility(str) -> str
# purpose: Handles game state transitions in compatibility mode.
#          Runs game state based on input (gameState)
#          Always returns quit when the game state returns quit
# examples:
#          setGameStateCompatibility("mainMenu") -> "quit"
#          setGameStateCompatibility("game state that doesnt exist") -> "quit"
#          setGameStateCompatibility("") -> "quit"
def setGameStateCompatibility(gameState):
    return "quit"

# setGameStateCompatibility(str) -> str
# purpose: Handles game state transitions in regular mode. Runs game
#          state based on input (gameState) Always returns quit when
#          the game state returns or a inccorect game state is recieved
# examples:
#          setGameStateCompatibility("mainMenu") -> "quit"
#          setGameStateCompatibility("game state that doesnt exist") -> "quit"
#          setGameStateCompatibility("") -> "quit"
def setGameStateRegular(gameState):
    match gameState:
        case "mainMenu":
            return regularMainMenu.main()
        case "htp":
            return regularHtpMenu.main()
        case "playMenu":
            return regularPlayMenu.main(coins)
    
    helperFuncs.clearTerminal()
    print(gameState)
    return "quit"

# main() -> None
# purpose: Game starts here here, sets launch mode, and starts the main game loop.
# examples:
#          main() -> None
def main():
    gameState = "mainMenu"

    # clear before starting
    helperFuncs.clearTerminal()

    # TODO: uncomment
    isRegularMode = launchMode.main()
    # get launch mode and start game after
    # if os.name == "nt":
    #     isRegularMode = launchMode.main()i
    # else:
    #     isRegularMode = False

    while gameState != "quit":
        if isRegularMode:
            gameState = setGameStateRegular(gameState)
        else:
            gameState = setGameStateCompatibility(gameState)

main()