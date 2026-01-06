import launchMode
import Input
import regularMainMenu
import os

def main():
    gameState = ""

    # clear before starting
    os.system('clear')

    # get launch mode
    isRegularMode = launchMode.main()

    # if regular mode
    if isRegularMode:
        gameState = regularMainMenu.main()

    print(gameState)

main()