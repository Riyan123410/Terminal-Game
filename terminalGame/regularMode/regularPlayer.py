import player
import userInput
import helperFuncs
from asciiArt import asciiHelpers
from asciiArt import asciiMenus
from asciiArt import asciiEnemies

# game constants
MAX_HAND = 14

# menu constants
MENU_DIR_X = "xDir"
MENU_DIR_Y = "yDir"
DECKS_MAX = 2
MENU_MIN = 0
ARROW_MIN = 1
IS_COMPATIBILITY_MODE = False

# menu up and down constants
Y_MIN = 0
Y_MAX = 1

def main():
    won = player.gameLoop(IS_COMPATIBILITY_MODE)
    if won:
        return "won"
    return "lost"


# selectCard([str], bool) -> str
# purpose: allows the player to select a card from their hand using input
#          the card pool that can be selected from is the parameter (cards)
#          it also prints the controls so the parameter (isDiscarding) is ued
#          in order to print the correct controls
def selectCard(cards, isDiscarding):
    currentSelectedY = 0

    currentMaxHand = len(cards) - 1
    currentSelected = MENU_MIN
    # first display with first deck selected and make card selected deck + 1 so it isnt selected
    selected = asciiHelpers.displayMainPlay(
        cards, 
        DECKS_MAX + 1, 
        currentSelected,
        (MENU_MIN, currentMaxHand),
        (Y_MIN, Y_MAX),
        currentSelectedY,
        isDiscarding)
    # if its not -1(nothing selected) than return the card selected
    if selected[0] != -1:
        return cards[selected[0]]
    currentSelectedY = selected[1]

    # the while loop didnt catch any card being selected so return none
    return None

# choose to look at the deck
def selectDeck(cards, isDiscarding):
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
        isDiscarding)
    
    # first option is the deck, the other is discard if selected display it
    match selected[0]:
        case 0:
            asciiHelpers.displayDeck(player.deck)
        case 1:
            asciiHelpers.displayDeck(player.discard)
        case 2:
            return "end"
    # update y and end is not selected so return none
    currentSelectedY = selected[1]
    return "None"


# getCardSelected([str], bool) -> str
# purpose: loops until a card is selected by the player and returns it
#          the card pool is from the list (cards) and also needs to print
#          the controls so (isDiscarding) is used to print the correct
def getCardSelected(cards, isDiscarding):
    # global variables
    global currentSelectedY

    card = "None"
    currentSelectedY = Y_MIN
    # loop forever until a card is selected
    while True:
        if currentSelectedY == Y_MIN:
            card = selectCard(cards, isDiscarding)
        else:
            card = selectDeck(cards, isDiscarding)
        # when recieving an input check if its a real card to return
        if card != None:
            return card

# getEnemySelected() -> str
# purpose: lets the player select an enemy from the current list using input
def getEnemySelected():
    # get max from enemy list
    enemyList = list(player.enemies.keys())
    enemyMax = len(enemyList)
    currentSelected = ARROW_MIN

    printEnemySelection(currentSelected, enemyMax)

    while True:
        inputList = userInput.getInputList()
        # add one to menu min since arrow starts at 1 not 0
        currentSelected = helperFuncs.changeWithClamp(currentSelected, inputList[MENU_DIR_X], ARROW_MIN, enemyMax)
        printEnemySelection(currentSelected, enemyMax)
        
        # when selected return enemy - 1 since arrow at 1 not 0
        if inputList["space"]:
            return enemyList[currentSelected - 1]
        
# printEnemySelection(int, int) -> None
# purpose: displays enemies, selection arrow, and controls in the terminal
#          the arrow starts at the input (currentSelected) and the max the
#          arrow does depends on the enemy max with the parameter (enemyMax)
def printEnemySelection(currentSelected, enemyMax):
    helperFuncs.clearTerminal()
    indexToArrow = asciiHelpers.indexToArrow(currentSelected, enemyMax, asciiEnemies.arrow["blank"], asciiEnemies.arrow["arrow"],asciiEnemies.arrow["arrow"])

    # print the enemys on top, than the selection arrow and finally the controls
    asciiHelpers.displayEnemies()
    print(asciiHelpers.combineCardStrings(indexToArrow, asciiEnemies.ARROW_HEIGHT))
    print(asciiMenus.getPlayControls("selectEnemy", player.cost, player.playerBlock, player.playerHealth))