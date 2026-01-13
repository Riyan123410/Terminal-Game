import launchMode
import helperFuncs
import gameCredits
import endGame
import player
# https://docs.python.org/3/tutorial/modules.html
from regularMode import regularShop
from regularMode import regularPlayer
from regularMode.menus import regularMainMenu
from regularMode.menus import regularHtpMenu
from regularMode.menus import regularPlayMenu


# setGameStateCompatibility(str) -> str
# purpose: Handles game state transitions in compatibility mode.
#          Runs game state based on input (gameState)
#          Always returns quit when the game state returns quit
def setGameStateCompatibility():
    # true for compatability mode
    player.gameLoop(True)
    print("game over - quitting")
    return "quit"

# setGameStateCompatibility(str) -> str
# purpose: Handles game state transitions in regular mode. Runs game
#          state based on input (gameState) Always returns quit when
#          the game state returns or a inccorect game state is recieved
def setGameStateRegular(gameState):
    # match each gamestate to their corresponding game state and return it
    match gameState:
        case "mainMenu":
            return regularMainMenu.main()
        case "htp":
            return regularHtpMenu.main()
        case "credits":
            return gameCredits.main()
        case "playMenu":
            return regularPlayMenu.main()
        case "shop":
            return regularShop.main()
        case "regularPlay":
            return regularPlayer.main()
        case "won":
            return endGame.win()
        case "lost":
            return endGame.lose()
        case _:
            pass
    # if not game state match print it and return "quit"
    print(gameState)
    return "quit"

# main() -> None
# purpose: Game starts here here, sets launch mode, and runs the main game loop.
def main():
    # set default game state
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
    

    # run the game until a game sate returns quit
    while gameState != "quit":
        if isRegularMode:
            gameState = setGameStateRegular(gameState)
        else:
            gameState = setGameStateCompatibility()

# run main
main()
