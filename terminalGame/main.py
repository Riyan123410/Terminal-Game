import launchMode
import Input
import os
from regularMode.menus import regularMainMenu

def main():
    gameState = ""

    # clear before starting
    os.system('clear')

    # get launch mode
    isRegularMode = launchMode.main()

    # if regular mode
    if isRegularMode:
        gameState = regularMainMenu.main()
    
    # check each game state
    match gameState:
        case "htp":
            pass


    print(gameState)

main()