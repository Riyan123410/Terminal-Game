import player
import userInput
import helperFuncs
from asciiArt import asciiHelpers
from asciiArt import asciiMenus
from asciiArt import asciiEnemies

# game constants
MAXHAND = 14

# menu constants
MENUDIRX = "xDir"
MENUDIRY = "yDir"
DECKSMAX = 2
MENUMIN = 0
ARROWMIN = 1
ISCOMPATIBILITYMODE = False

# menu variables
currentSelectedY = 0

# menu up and down constants
YMIN = 0
YMAX = 1

# main() -> string
# purpose: starts the players main gameLoop, gets if you won the game,
#          if you won, return "won" else return "lost"
def main():
    won = player.gameLoop(ISCOMPATIBILITYMODE)
    if won:
        return "won"
    return "lost"


# selectCard([str], bool) -> str
# purpose: allows the player to select a card from their hand using input
#          the card pool that can be selected from is the parameter (cards)
#          it also prints the controls so the parameter (isDiscarding) is ued
#          in order to print the correct controls. Returns the card that is 
#          selected if no card is selected "None" is returned. INFO: make sure
#          cards is in the dictionary asciiCards.art or a key not found error
#          will occur
def selectCard(cards, isDiscarding):
    # get global selected y
    global currentSelectedY

    # the current max hand is the len of cards - 1 since lists start at - 0
    currentMaxHand = len(cards) - 1
    currentSelected = MENUMIN

    # first display with first deck selected and make card selected deck + 1 so it isnt selected
    selected = asciiHelpers.displayMainPlay(
        cards, 
        DECKSMAX + 1, 
        currentSelected,
        (MENUMIN, currentMaxHand),
        (YMIN, YMAX),
        currentSelectedY,
        isDiscarding)
    # if its not -1(nothing selected) than return the card selected
    if selected[0] != -1:
        return cards[selected[0]]
    currentSelectedY = selected[1]

    # no card was selected so return "None"
    return "None"


# selectCard([str], bool) -> str
# purpose: allows the player to look at a deck using input or to select
#          end turn. It also displays the currents cards from the parameter
#          (cards) and the parameter (isDiscarding) is used to print the
#          appropiate instructoins to the user. INFO: make sure
#          cards is in the dictionary asciiCards.art or a key not found error
#          will occur
def selectDeck(cards, isDiscarding):
    # get global current selected y
    global currentSelectedY
    currentSelected = MENUMIN

    # first display with first deck selected and make card selected deck + 1 so it isnt selected
    selected = asciiHelpers.displayMainPlay(
        cards, 
        currentSelected, 
        MAXHAND + 1, 
        (MENUMIN, DECKSMAX),
        (YMIN, YMAX), 
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
#          the controls so (isDiscarding) is used to print the correct. INFO: make sure
#          cards is in the dictionary asciiCards.art or a key not found error
#          will occur
def getCardSelected(cards, isDiscarding):
    # global variables
    global currentSelectedY

    # current card is nont and reset current selcted y
    card = "None"
    currentSelectedY = YMIN

    # loop forever until a card is selected
    while True:
        # select a card
        if currentSelectedY == MENUMIN:
            card = selectCard(cards, isDiscarding)
        else:
            card = selectDeck(cards, isDiscarding)
        # when recieving an input check if its a real card to return
        if card != "None":
            return card

# getEnemySelected() -> str
# purpose: lets the player select an enemy from the current list using input
def getEnemySelected():
    # get max from enemy list
    enemyList = list(player.enemies.keys())
    enemyMax = len(enemyList)
    currentSelected = ARROWMIN

    # print enemys
    printEnemySelection(currentSelected, enemyMax)

    # loop until input
    while True:
        inputList = userInput.getInputDict()
        # add one to menu min since arrow starts at 1 not 0
        currentSelected = helperFuncs.changeWithClamp(currentSelected, inputList[MENUDIRX], ARROWMIN, enemyMax)
        printEnemySelection(currentSelected, enemyMax)
        
        # when selected return enemy - 1 since arrow at 1 not 0
        if inputList["space"]:
            return enemyList[currentSelected - 1]
        
# printEnemySelection(int, int) -> None
# purpose: displays enemies, selection arrow, and controls in the terminal
#          the arrow starts at the input (currentSelected) and the max the
#          arrow does depends on the enemy max with the parameter (enemyMax)
def printEnemySelection(currentSelected, enemyMax):
    # clear terminal than get arrow string from index
    helperFuncs.clearTerminal()
    indexToArrow = asciiHelpers.indexToArrow(currentSelected, enemyMax, asciiEnemies.arrow["blank"], asciiEnemies.arrow["arrow"],asciiEnemies.arrow["arrow"])

    # print the enemys on top, than the selection arrow and finally the controls
    asciiHelpers.displayEnemies()
    print(asciiHelpers.combineCardStrings(indexToArrow, asciiEnemies.ARROWHEIGHT))
    print(asciiMenus.getPlayControls("selectEnemy", player.cost, player.playerBlock, player.playerHealth))