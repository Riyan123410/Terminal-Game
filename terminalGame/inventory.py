import player

coins = 0
cards = ["strike", "strike", "strike", "strike", "strike", "strike", "block", "block", "block", "crossbow"]
DEFAULT_CARDS = ["strike", "strike", "strike", "strike", "strike", "strike", "block", "block", "block", "crossbow", "clean sweep"]
DEFAULT_COINS = 0

def resetInventory():
    global coins
    global cards
    coins = DEFAULT_COINS
    cards = DEFAULT_CARDS
    player.difficulty = 0.5
    player.enemies = dict({})