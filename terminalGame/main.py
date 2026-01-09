import launchMode
import os
import helperFuncs
import userInput
import gameCredits
from regularMode import regularShop
from regularMode.menus import regularMainMenu
from regularMode.menus import regularHtpMenu
from regularMode.menus import regularPlayMenu


# setGameStateCompatibility(str) -> str
# purpose: Handles game state transitions in compatibility mode.
#          Runs game state based on input (gameState)
#          Always returns quit when the game state returns quit
# examples:
#          setGameStateCompatibility("mainMenu") -> "quit"
#          setGameStateCompatibility("game state that doesnt exist") -> "quit"
#          setGameStateCompatibility("") -> "quit"
def setGameStateCompatibility(gameState):
    helperFuncs.clearTerminal()
    print(gameState)
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
        case "credits":
            return gameCredits.main()
        case "playMenu":
            return regularPlayMenu.main()
        case "gameLoop":
            return player.gameLoop()
        case "shop":
            return regularShop.main()
    
    print(gameState)
    return "quit"

# main() -> None
# purpose: Game starts here here, sets launch mode, and starts the main game loop.
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

    # set game state based on compatability mode
    if isRegularMode:
        setGameState = setGameStateRegular
    else:
        setGameState = setGameStateCompatibility

    # run the game until a game sate returns quit
    while gameState != "quit":
        gameState = setGameState(gameState)

main()