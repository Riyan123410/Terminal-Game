import launchMode
import Input
import regularMainMenu

mode = launchMode.main()
gameState = ""

# regular mode
if mode == 0:
    gameState = regularMainMenu.main()

print(gameState)