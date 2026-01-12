import player

DEFAULT_CARDS = ["strike", "strike", "strike", "strike", "strike", "block", "block", "block", "block", "block", "crossbow", "supressive fire"]
DEFAULT_COINS = 0
DIFFICULTY_COINS_CONVERSION = 2

cards = DEFAULT_CARDS.copy()
coins = DEFAULT_COINS

def resetInventory():
    global coins
    global cards
    global DEFAULT_CARDS
    global DEFAULT_COINS
    coins = DEFAULT_COINS
    cards = DEFAULT_CARDS.copy()
    player.difficulty = 0.5
    player.enemies = dict({})