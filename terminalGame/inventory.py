import player

DEFAULT_CARDS = ["strike", "strike", "strike", "strike", "strike", "block", "block", "block", "block", "block", "crossbow"]
DEFAULT_COINS = 0
DIFFICULTY_COINS_CONVERSION = 2.5

cards = DEFAULT_CARDS.copy()
coins = DEFAULT_COINS

# resetInventory() -> None
# purpose: resets the players inventory including coins, cards
#          and difficulty to their default values
def resetInventory():
    global coins
    global cards
    global DEFAULT_CARDS
    global DEFAULT_COINS
    coins = DEFAULT_COINS
    cards = DEFAULT_CARDS.copy()
    player.difficulty = player.DIFFICULTY_START
    player.enemies = dict({})