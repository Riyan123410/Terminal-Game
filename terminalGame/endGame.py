import player
import inventory

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
    player.difficulty += player.DIFFICULTY_MODIFIER
    inventory.coins += difficulty * 10
    input()
    return "playMenu"

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
    input()
    inventory.resetInventory()
    return "mainMenu"