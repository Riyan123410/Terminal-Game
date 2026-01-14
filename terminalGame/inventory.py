import player

DEFAULTCARDS = ["strike", "strike", "strike", "strike", "strike", "block", "block", "block", "block", "block", "crossbow", "sonic speed"]
DEFAULTCOINS = 0
DIFFICULTYCOINSCONVERSION = 2.5

# https://www.w3schools.com/python/ref_list_copy.asp
cards = DEFAULTCARDS.copy()
coins = DEFAULTCOINS

# resetInventory() -> None
# purpose: resets the players inventory including coins, cards
#          and difficulty to their default values
def resetInventory():
    # get global variables
    global coins
    global cards
    global DEFAULTCARDS
    global DEFAULTCOINS
    coins = DEFAULTCOINS
    cards = DEFAULTCARDS.copy()
    player.difficulty = player.DIFFICULTYSTART
    player.enemies = dict({})