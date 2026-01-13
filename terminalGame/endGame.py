import player
import inventory
from regularMode import regularShop


# win() -> None
# purpose: the victory screen for when the player wins a round, it prints the
#          current difficulty as well. Changes the diff for next round, give coins
#          resets effects, restocks the stop and waits for input to exit
def win():
    difficulty = player.difficulty
    print(rf"""
 ___      ___ ___  ________ _________  ________  ________      ___    ___ ___       
|\  \    /  /|\  \|\   ____\\___   ___\\   __  \|\   __  \    |\  \  /  /|\  \      
\ \  \  /  / | \  \ \  \___\|___ \  \_\ \  \|\  \ \  \|\  \   \ \  \/  / | \  \     
 \ \  \/  / / \ \  \ \  \       \ \  \ \ \  \\\  \ \   _  _\   \ \    / / \ \  \    
  \ \    / /   \ \  \ \  \____   \ \  \ \ \  \\\  \ \  \\  \|   \/  /  /   \ \__\   
   \ \__/ /     \ \__\ \_______\  \ \__\ \ \_______\ \__\\ _\ __/  / /      \|__|   
    \|__|/       \|__|\|_______|   \|__|  \|_______|\|__|\|__|\___/ /           ___ 
                                                             \|___|/           |\__\
                                                                               \|__|
                            Current Score: {difficulty}
[ENTER] to continue
""")
    # increase ifficulty and coins
    player.difficulty += player.DIFFICULTYMODIFIER
    inventory.coins += player.difficulty * inventory.DIFFICULTYCOINSCONVERSION
    # reset plater and restock shop
    player.resetEffects()
    regularShop.resetStock()

    # wait for input to go back
    input()
    return "playMenu"


# lose() -> None
# purpose: the lose screen for when the player loses a round, it prints the
#          current difficulty and high score as well. resets the diff for next round, resets coins
#          resets effects, restocks the stop and waits for input to exit
def lose():
    # read the current high score and close the file
    readDifficultyFile = open("difficulty.txt", "r")
    highScore = float(readDifficultyFile.read())
    readDifficultyFile.close()
    # if difficulty is higher than high score write the new highscore
    if player.difficulty > highScore:
        highScore = player.difficulty
        readDifficultyFile = open("difficulty.txt", "w")
        readDifficultyFile.write(str(highScore))
        readDifficultyFile.close()
    print(rf"""
    ________  _______   ________ _______   ________  _________   
    |\   ___ \|\  ___ \ |\  _____\\  ___ \ |\   __  \|\___   ___\ 
    \ \  \_|\ \ \   __/|\ \  \__/\ \   __/|\ \  \|\  \|___ \  \_| 
     \ \  \ \\ \ \  \_|/_\ \   __\\ \  \_|/_\ \   __  \   \ \  \  
      \ \  \_\\ \ \  \_|\ \ \  \_| \ \  \_|\ \ \  \ \  \   \ \  \ 
       \ \_______\ \_______\ \__\   \ \_______\ \__\ \__\   \ \__\
        \|_______|\|_______|\|__|    \|_______|\|__|\|__|    \|__|

                        Score: {player.difficulty}
                        High Score: {highScore}
                                                              
    [ENTER] to continue                                                        
""")
    # wait for input than reset inv and effect than exit
    input()
    inventory.resetInventory()
    player.resetEffects()
    return "mainMenu"