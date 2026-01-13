import player

DEFAULTCARDS = ["strike", "strike", "strike", "strike", "strike", "block", "block", "block", "block", "block", "crossbow"]
DEFAULTCOINS = 0
DIFFICULTYCOINSCONVERSION = 2.5

cards = DEFAULTCARDS.copy()
coins = DEFAULTCOINS

# resetInventory() -> None
# purpose: resets the players inventory including coins, cards
#          and difficulty to their default values
def resetInventory():
    global coins
    global cards
    global DEFAULTCARDS
    global DEFAULTCOINS
    coins = DEFAULTCOINS
    cards = DEFAULTCARDS.copy()
    player.difficulty = player.DIFFICULTYSTART
    player.enemies = dict({})