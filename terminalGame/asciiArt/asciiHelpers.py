import helperFuncs
import userInput
import player
from asciiArt import asciiCards
from asciiArt import asciiHelpers
from asciiArt import asciiEnemies
from asciiArt import asciiMenus


MAX_CARD_LENGTH = 7

# findWidth(str) -> int
# purpose: calculates the width of an ASCII string by finding the first \n character after the first line
#          from the inputed string (string)
# examples:
#          findWidth("abc\n") -> 3
#          findWidth("a\bc\df\n") -> 1
#          findWidth("\n\n") -> 0
def findWidth(string):
    # replace endlines so you can find it not starting at the begining since that is an endline
    replaceEndlines = string.replace("\n", "~")
    # has to be a symbol not being used from ascii art
    width = replaceEndlines.find("~", 1) - 1
    if width < 0:
        width = 0
    return width

# combineStrings(str, str, int, int) -> str
# purpose: combines two ASCII strings horizontally given their widths and height
#          from the parameters (width1) and (height) the strings are also given
#          with parameter (string1) which would be on the left and (string2)
#          which would be on the right
# examples:
#          combineStrings("abc\n", "123\n", 3, 1) -> "abc123\n"
#          combineStrings("a\nb\n", "x\ny\n", 1, 2) -> "ax\nby\n"
#          combineStrings("", "x\n", 0, 1) -> "x\n"
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

# combineCardStrings([str], int) -> str
# purpose: combines a list of ASCII card strings horizontally into one large string
#          with the parameter (cards) being a list of strings and the height is also
#          required with the parameter (height)
# examples:
#          combineCardStrings(["abc\n", "123\n"], 1) -> "abc123\n"
#          combineCardStrings([], 1) -> ""
#          combineCardStrings(["a\n", "b\n", "c\n"], 1) -> "abc\n"
def combineCardStrings(cards, height):
    # set string and len
    combinedString = ""
    width = 0
    # loop through each card and add them
    for card in cards:
        combinedString = combineStrings(combinedString, card, width, height)
        width += findWidth(card)

    return combinedString

# splitHand([str], int) -> ([str], [str])
# purpose: splits a hand of cards of parameter (totalHand) into two lists 
#          if is is more than the parameter (maxLen)
# examples:
#          splitHand(["a","b","c"], 2) -> (["a","b"], ["c"])
#          splitHand(["x","y"], 3) -> (["x","y"], [])
#          splitHand([], 1) -> ([], [])
def splitHand(totalHand, maxLen):
    newRow = []
    # loop through the hand remove and adding until your hand is less than the max
    while len(totalHand) > maxLen:
        newRow.append(totalHand[-1])
        totalHand.pop()
    # revers the 2nd list since we are adding to it backwards
    newRow.reverse()
    return (totalHand, newRow)

# createAsciiCardList([str], int) -> [str]
# purpose: creates a list of ASCII card art strings from a list of
#          card names inputed withe the parameter (cards) the paremter
#          (currentSelected) will use a different artwork
# examples:
#          createAsciiCardList(["strike"], 0) -> ["selected strike art"]
#          createAsciiCardList(["block"], 1) -> ["normal block art"]
#          createAsciiCardList([], 0) -> []
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

# displayCards([str]) -> None
# purpose: prints a hand of cards with parameter (cards) in rows with ASCII art
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

# displayDeck([str]) -> None
# purpose: prints each card in a deck as selected ASCII art and waits for user input
#          the cards printed will be a list of strings (deck)
def displayDeck(deck):
    helperFuncs.clearTerminal()
    for card in deck:
        print(asciiCards.art[card]["selected"])
    print("[ENTER] to continue")
    input()

# numToString(int) -> str
# purpose: converts a number (num) into a string compatible with ASCII enemies
#          (adds leading zero if < 10)
# examples:
#          numToString(5) -> "05"
#          numToString(12) -> "12"
#          numToString(0) -> "00"
def numToString(num):
    string = ""
    if num < 10:
        string += "0"
    return string + str(num)

# displayEnemies() -> None
# purpose: prints all enemies using ASCII art and prints them horizontally
def displayEnemies():
    enemies = player.enemies
    stringList = []
    for enemy in enemies.keys():
        stringList.append(asciiEnemies.getArt(enemy, enemies[enemy]["health"]))
    print(asciiHelpers.combineCardStrings(stringList, asciiEnemies.ENEMY_HEIGHT))


# indexToArrow(int, int, str, str, str) -> [str]
# purpose: creates a list of strings representing arrows for menu selection
# examples:
#          indexToArrow(1, 3, "-", ">", "^") -> [">", "-", "-"]
#          indexToArrow(2, 3, "-", ">", "^") -> ["-", ">", "-"]
#          indexToArrow(3, 3, "-", ">", "^") -> ["-", "-", "^"]
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