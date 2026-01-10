import helperFuncs
import userInput
import player
from asciiArt import asciiCards
from asciiArt import asciiHelpers
from asciiArt import asciiEnemies
from asciiArt import asciiMenus


MAX_CARD_LENGTH = 7

def findWidth(string):
    # replace endlines so you can find it not starting at the begining since that is an endline
    replaceEndlines = string.replace("\n", "~")
    # has to be a symbol not being used from ascii art
    width = replaceEndlines.find("~", 1) - 1
    if width < 0:
        width = 0
    return width

def combineStrings(string1, string2, width1, height):
    # find width of strings
    width2 = findWidth(string2)
    # remove all end lines and create a new string
    string1 = string1.replace("\n", "")
    string2 = string2.replace("\n", "")
    combinedString = ""
    # loop through the height of the strings
    for i in range(height):
       # loop through the legnth of each adding to the new string
        combinedString += string1[i * width1 : i * width1 + width1]
        combinedString += string2[i * width2 : i * width2 + width2]
        combinedString += "\n"
    return combinedString

def combineCardStrings(cards, height):
    # set string and len
    combinedString = ""
    width = 0
    # loop through each card and add them
    for card in cards:
        combinedString = combineStrings(combinedString, card, width, height)
        width += findWidth(card)

    return combinedString

# split hand you hand into 2 lists
def splitHand(totalHand, maxLen):
    newRow = []
    # loop through the hand remove and adding until your hand is less than the max
    while len(totalHand) > maxLen:
        newRow.append(totalHand[-1])
        totalHand.pop()
    # revers the 2nd list since we are adding to it backwards
    newRow.reverse()
    return (totalHand, newRow)

# with a list of all the items create a string list with ascii art
def createAsciiCardList(cards, currentSelected):
    asciiDeck = []
    # loop throught the car dlist
    for i in range(len(cards)):
        # check if this card is selected and add that card art
        cardArt = "normal"
        if i == currentSelected:
            cardArt = "selected"

        asciiDeck.append(str(asciiCards.art[cards[i]][cardArt]))
    return asciiDeck

# menuLoop(int, dict, str, (), function) -> str
# purpose: The menu loop that handles input, selection, ASCII art display,
#          and returns the next game state. To do this it needs the starting
#          selecting with (currentSelected), the direction the menu is going
#          in (menuDir) can be "xDir" or "yDir" making it accept WS or AD input, 
#          the range (menuRange) of the optns and (nextStates) for a list of 
#          all possible game states the menu can lead to in order
# examples:
#          menuLoop(2, "yDir", (0, 2), getMainMenuArt, ("play", "shop", "mainMenu")) -> "mainMenu"
#          menuLoop(0, "xDir", (0, 3), getPlayMenuArt, ("quit", "credits", "htp", "playMenu")) -> "quit"
def menuLoop(currentSelected, menuDir, menuRange, artFunc, nextStates):

    # reset terminal and try to print art function
    helperFuncs.clearTerminal()
    try:
        print(artFunc()[currentSelected])
    except:
        print("art function is incorrect")
    
    while True:
        # try to change menu
        inputList = userInput.getInputList()
        try:
            currentSelected = helperFuncs.changeWithClamp(currentSelected, inputList[menuDir], menuRange[0], menuRange[1])
        except:
            print("user input is incorrect")
        
        # if selected return next state
        if inputList["space"]:
            return nextStates[currentSelected]
        
        # try to update menu
        helperFuncs.clearTerminal()
        try:
            print(artFunc()[currentSelected])
        except:
            print("function for ascii art is out of range")

# actually print the cards
def displayCards(cards):
    hand = splitHand(cards, MAX_CARD_LENGTH)
    print(combineCardStrings(hand[0], asciiCards.CARD_HEIGHT))
    # make sure your hand isn't empty before printing
    if hand[1] != ():
        print(combineCardStrings(hand[1], asciiCards.CARD_HEIGHT))

def printPlayMain(cards, cardSelected, deckSelected, isDiscarding):
    # first display with first deck selected and make card selected deck + 1 so it isnt selected
    helperFuncs.clearTerminal()
    displayEnemies()
    print(asciiCards.getDeckArt()[deckSelected])
    displayCards(createAsciiCardList(cards, cardSelected))
    # depending on if you are discarding print those contorls
    if isDiscarding:
        print(asciiMenus.playControls["discardCard"])
    else:
        print(asciiMenus.playControls["playCard"])


# actually call this in order to print the play menu
def displayMainPlay(cards, deckSelected, cardSelected, menuRange, yRange, currentSelectedY, isDiscarding):

    printPlayMain(cards, cardSelected, deckSelected, isDiscarding)
    menuY = currentSelectedY
    currentSelected = menuRange[0]

    while currentSelectedY == menuY:
        # update current selected
        inputList = userInput.getInputList()
        currentSelected = helperFuncs.changeWithClamp(currentSelected, inputList["xDir"], menuRange[0], menuRange[1])
        # check if we are on the deck or card menu than cange that selected
        if menuY == 1:
            deckSelected = currentSelected
        else:
            cardSelected = currentSelected
        
        # return if space is pressed
        if inputList["space"]:
            return (currentSelected, currentSelectedY)

        # print
        asciiHelpers.printPlayMain(cards, cardSelected, deckSelected, isDiscarding)

        # if the y is going down make current selected fo down
        currentSelectedY = helperFuncs.changeWithClamp(currentSelectedY, inputList["yDir"],yRange[0], yRange[1])
    # none actually selected so return it as -1
    currentSelected = -1
    return (currentSelected, currentSelectedY)


def displayDeck(deck):
    helperFuncs.clearTerminal()
    for card in deck:
        print(asciiCards.art[card]["selected"])
    print("[ENTER] to continue")
    input()

# makes numbers compatable with ascii enemies
def numToString(num):
    string = ""
    if num < 10:
        string += "0"
    return string + str(num)

# print enemies
def displayEnemies():
    enemies = player.enemies
    stringList = []
    for enemy in enemies.keys():
        stringList.append(asciiEnemies.getArt(enemy, enemies[enemy]["health"]))
    print(asciiHelpers.combineCardStrings(stringList, asciiEnemies.ENEMY_HEIGHT))


def indexToArrow(currentSelected, menuMax, blankString, arrowString, lastArrow):
    # create empty list
    arrowList = []
    # based on index subtract one to make a space for the arrow
    for i in range(currentSelected - 1):
        arrowList.append(blankString)
    # add the arrow and return the list
    if currentSelected == menuMax:
        arrowList.append(lastArrow)
    else:
        arrowList.append(arrowString)
    return arrowList