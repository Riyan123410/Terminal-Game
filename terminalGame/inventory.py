import player

DEFAULT_CARDS = ["strike", "strike", "strike", "strike", "strike", "block", "block", "block", "block", "block", "crossbow",]
DEFAULT_COINS = 0
COINS_MODIFIER = 3

cards = DEFAULT_CARDS
coins = 0

def resetInventory():
    global coins
    global cards
    coins = DEFAULT_COINS
    cards = DEFAULT_CARDS.copy()
    player.difficulty = 0.5
    player.enemies = dict({})