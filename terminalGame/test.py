import userInput
import helperFuncs
from asciiArt import asciiCards
from asciiArt import asciiHelpers

# variables
hand = ["strike", "strike", "strike", "strike", "strike", "strike", "strike", "strike", "strike"]
deck = ["strike", "strike", "strike"]
discard = ["strike", "strike"]
enemies = ["bush", "wild bush", "goose", "tree", "goose"]
currentSelectedY = 0
currentMaxHand = len(hand) - 1

isCompatabilityMode = False

# game constants
MAX_HAND = 14

# menu constants
MENU_DIR_X = "xDir"
MENU_DIR_Y = "yDir"
DECKS_MAX = 1
MENU_MIN = 0

# menu up and down constants
Y_MIN = 0
Y_MAX = 1


# actually choose and select the card with input
def selectCard(cards, enemies):
    global currentSelectedY
    currentSelected = MENU_MIN
    # first display with first deck selected and make card selected deck + 1 so it isnt selected
    selected = asciiHelpers.displayMainPlay(
        cards, 
        DECKS_MAX + 1, 
        currentSelected,
        (MENU_MIN, currentMaxHand),
        (Y_MIN, Y_MAX),
        currentSelectedY,
        enemies)
    # if its not -1(nothing selected) than return the card selected
    if selected[0] != -1:
        return cards[selected[0]]
    currentSelectedY = selected[1]

    # the while loop didnt catch any card being selected so return none
    return "None"

# choose to look at the deck
def selectDeck(cards, enemies):
    global currentSelectedY
    currentSelected = MENU_MIN
    # first display with first deck selected and make card selected deck + 1 so it isnt selected
    selected = asciiHelpers.displayMainPlay(
        cards, 
        currentSelected, 
        MAX_HAND + 1, 
        (MENU_MIN, DECKS_MAX),
        (Y_MIN, Y_MAX), 
        currentSelectedY,
        enemies)
    
    # first option is the deck, the other is discard if selected display it
    if selected[0] == 0:
        asciiHelpers.displayDeck(deck)
    if selected[0] == 1:
        asciiHelpers.displayDeck(discard)

    # update y
    currentSelectedY = selected[1]

def getCardSelected(cards, enemies):
    # global variables
    global currentSelectedY

    card = "None"
    currentSelectedY = Y_MIN
    # loop forever until a card is selected
    while True:
        if currentSelectedY == Y_MIN:
            card = selectCard(cards, enemies)
        else:
            selectDeck(cards, enemies)
        # when recieving an input check if its a real card to return
        if card != "None":
            return card

getCardSelected(hand, enemies)