import helperFuncs
import userInput
import player
from asciiArt import asciiCards
from asciiArt import asciiHelpers
from asciiArt import asciiEnemies
from asciiArt import asciiMenus


MAXCARDLENGTH = 7

# findWidth(string) -> int
# purpose: calculates the width of an ASCII string by finding the first \n character after the first line
#          from the inputed string (string), so if it doesnt start at \n width will be 1 less
#          make sure string starts with \n to count properly and has a second \n or width will be 0
# examples:
#          findWidth("abc\n") -> 2
#          findWidth("a\bc\df\n") -> 7
#          findWidth("\n\n") -> 0
def findWidth(string):
    # replace endlines so you can find it not starting at the begining since that is an endline
    replaceEndlines = string.replace("\n", "~")
    # has to be a symbol not being used from ascii art
    width = replaceEndlines.find("~", 1) - 1
    if width < 0:
        width = 0
    return width

# tests for findWidth
assert findWidth("hello\nworld") == 4
assert findWidth("\nhello") == 0
assert findWidth("abc\ndef\nghi") == 2
assert findWidth("singleline") == 0
assert findWidth("\n") == 0
assert findWidth("") == 0
assert findWidth("a\nb\nc\n") == 0


# combineStrings(string, string, int, int) -> string
# purpose: combines two ASCII strings horizontally given their widths and height
#          from the parameters (width1) and (height) the strings are also given
#          with parameter (string1) which would be on the left and (string2)
#          which would be on the right. Make sure width1 is entered correctly,
#          ascii starts with \n, ends with \n, height is entered correctly or
#          it wont wrap as expected
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
       # add each string using slicing from i to width
       # https://www.w3schools.com/python/gloss_python_string_slice.asp
        combinedString += string1[i * width1 : i * width1 + width1]
        combinedString += string2[i * width2 : i * width2 + width2]
        combinedString += "\n"
    return combinedString

# tests for combineStrings
assert combineStrings("\nab\ncd", "\n12\n34", 2, 2) == "ab12\ncd34\n"
assert combineStrings("\nhello\nworld", "idk", 5, 2) == "hello\nworld\n"
assert combineStrings("", "", 0, 0) == ""
assert combineStrings("\nabc\n", "\n123\n", 3, 1) == "abc123\n"


# combineCardStrings([string], int) -> string
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

# tests for combine cardStrings
assert combineCardStrings(["\nab\ncd", "\n12\n34"], 2) == "ab12\ncd34\n"
assert combineCardStrings(["\nhello\nworld\n", ""], 2) == "hello\nworld\n"
assert combineCardStrings(["\nabc\n"], 1) == "abc\n"
assert combineCardStrings([], 0) == ""


# splitHand([string], int) -> ([string], [string])
# purpose: splits a hand of cards of parameter (totalHand) into a tuple of 2 index  
#          if is is more than the parameter (maxLen) which must be positive
#          (the first hand will be len of max len and the other will be the remainder)
# examples:
#          splitHand(["a","b","c"], 2) -> (["a","b"], ["c"])
#          splitHand(["x","y"], 3) -> (["x","y"], [])
#          splitHand([], 1) -> ([], [])
def splitHand(totalHand, maxLen):
    totalHandCopy = totalHand.copy()
    newRow = []
    # loop through the hand remove and adding until your hand is less than the max
    while len(totalHandCopy) > maxLen:
        newRow.append(totalHand[-1])
        totalHandCopy.pop()
    # revers the 2nd list since we are adding to it backwards
    # https://www.w3schools.com/python/ref_list_reverse.asp
    newRow.reverse()
    return (totalHandCopy, newRow)

# tests for splitHand
assert splitHand(["a", "b", "c"], 5) == (["a", "b", "c"], [])
assert splitHand(["a", "b", "c"], 3) == (["a", "b", "c"], [])
assert splitHand([], 3) == ([], [])


# createAsciiCardList([string], int) -> [string]
# purpose: creates a list of ASCII card art strings from a list of
#          card names inputed withe the parameter (cards) the paremter
#          (currentSelected) will use a different artwork. INFO make sure
#          cards is in dictionary asciiCards.art or it will give a key not
#          found error
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

# no tests because of ASCII art


# menuLoop(int, string, (int), function, (string)) -> string
# purpose: The menu loop that handles input, selection, ASCII art display,
#          and returns the next game state. To do this it needs the starting
#          selecting with (currentSelected), the direction the menu is going
#          in (menuDir) can be "xDir" or "yDir" making it accept WS or AD input, 
#          the range (menuRange) of the optns and (nextStates) for a list of 
#          all possible game states the menu can lead to in order.
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

# displayCards([string]) -> None
# purpose: prints a hand of cards with parameter (cards) in rows with ASCII art
def displayCards(cards):
    hand = splitHand(cards, MAXCARDLENGTH)
    print(combineCardStrings(hand[0], asciiCards.CARDHEIGHT))
    # make sure your hand isn't empty before printing
    if hand[1] != ():
        print(combineCardStrings(hand[1], asciiCards.CARDHEIGHT))


# printPlayMain([string], int, int, bool) -> None
# purpose: displays the main gameplay screen including enemies, the selected deck,
#          and the player's hand of cards with (cards). Highlights the currently selected 
#          card  or deck based on (cardSelected) and (deckSelected), and shows the appropriate 
#          control menu depending on whether the player is discarding a card (isDiscarding).
#          INFO: make sure cards is in the dictionary asciiCards.art or a key not found error
#          will be found
def printPlayMain(cards, cardSelected, deckSelected, isDiscarding):
    # first display with first deck selected and make card selected deck + 1 so it isnt selected
    helperFuncs.clearTerminal()
    displayEnemies()
    print(asciiCards.getDeckArt()[deckSelected])
    displayCards(createAsciiCardList(cards, cardSelected))
    # depending on if you are discarding print those contorls
    if isDiscarding:
        print(asciiMenus.getPlayControls("discardCard", player.cost, player.playerBlock, player.playerHealth))
    else:
        print(asciiMenus.getPlayControls("playCard", player.cost, player.playerBlock, player.playerHealth))


# displayMainPlay([string], int, int, (int, int), (int, int), int, bool) -> (int, int)
# purpose: handles the main gameplay input loop for selecting cards or decks.
#          with input (cards). starts selection with (deckSelected) and (cardSelected),  
#          and (currentSelectedY). Updates the current selection based on user input, and 
#          clamps selections with parameter (menuRange) and (yRange). Returns a tuple
#          of the currently selected item, -1 if none, and the current y based on input.
#          Finally prints the correct instructions with (isDiscarding)
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


# displayDeck([string]) -> None
# purpose: prints each card in a deck as selected ASCII art and waits for user input
#          the cards printed will be a list of strings (deck). INFO: make sure each string
#          in the list is in the dictionary asciiCards.art or a key not found error will
#          occur
def displayDeck(deck):
    helperFuncs.clearTerminal()
    for card in deck:
        print(asciiCards.art[card]["selected"])
    print("[ENTER] to continue")
    input()

# numToString(int) -> string
# purpose: converts a number (num) into a string compatible with ASCII enemies
#          (adds leading zero if < 10), no more formating needs to be done since
#          enemy HP is capped in game 1 to less than 100
# examples:
#          numToString(5) -> "05"
#          numToString(12) -> "12"
#          numToString(0) -> "00"
def numToString(num):
    string = ""
    # if less than 10 add 0 than return 
    if num < 10:
        string += "0"
    return string + str(num)

# tests for numToString
assert numToString(0) == "00"
assert numToString(5) == "05"
assert numToString(9) == "09"
assert numToString(10) == "10"
assert numToString(23) == "23"
assert numToString(100) == "100"

# displayEnemies() -> None
# purpose: prints all enemies using ASCII art horizontally
def displayEnemies():
    enemies = player.enemies
    stringList = []
    # loop through each enemy in enemy dict
    for enemy in enemies.keys():
        # put each enemy next to each other
        stringList.append(asciiEnemies.getArt(enemy, numToString(enemies[enemy]["health"]), formatDescriptionList(getAttackDescriptions(enemy))))
    print(asciiHelpers.combineCardStrings(stringList, asciiEnemies.ENEMYHEIGHT))

# no tests because ASCII art


# indexToArrow(int, int, string, string, string) -> [string]
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

# tests for indexToArrow
assert indexToArrow(1, 3, " ", ">", "*") == [">"]
assert indexToArrow(2, 3, " ", ">", "*") == [" ", ">"]
assert indexToArrow(3, 3, " ", ">", "*") == [" ", " ", "*"]
assert indexToArrow(1, 1, "-", "->", ">>") == ["->"]
assert indexToArrow(2, 2, "_", "=>", ">>") == ["_", ">>"]
assert indexToArrow(3, 5, ".", "->", "=>") == [".", ".", "->"]


# getAttackDescriptions(string) -> [string]
# purpose: Takes in a string called enemyName, then finds the attack descriptions for that specific enemy in the enemy list,
#           and returns them.
# examples:
#           getAttackDescriptions("goose") -> ["deal 2d4 damage", "Discard 1 card from your deck"]
#           getAttackDescriptions("bush")  -> [""]
def getAttackDescriptions(enemyName):
    enemies = player.enemies
    attackDescriptions = []
    # look through attacks and add them to attack descriptions
    for attack in enemies[enemyName]["attacks"]:
        attackDescriptions.append(attack["description"])
    return attackDescriptions


# tests for getAttackDescriptions



# formatDescription(string) -> string
# purpose: formats a string description (description) to fit in enemy
#          descriptions box defined by asciiEnemies.DESCRIPTIONLEN and asciiEnemies.DESCRIPTIONHEIGHT.
#          returnes the description with that cap len and that height ending with | on each line
def formatDescription(description):
    # get turn diescription strin ginto a list, set line and lines
    descriptionList = description.split().copy()
    line = ""
    lines = []

    for i in range(asciiEnemies.DESCRIPTIONHEIGHT):
        # reset index(wordsAdded) and overfill
        wordsAdded = 0
        overfill = False
        # get each word in the descpription loop until its overfilles
        while not overfill:
            # add it to the current line if its les than the max len than overfill, do a try just in case there is arent any words
            try:
                # add 2 because of extra space and | character
                if len(line) + len(descriptionList[wordsAdded]) + 2 < asciiEnemies.DESCRIPTIONLEN:
                    line += descriptionList[wordsAdded] + " "
                    wordsAdded += 1
                else:
                    overfill = True
            except:
                overfill = True
        # remove all words used
        for i in range(wordsAdded):
            descriptionList.pop(0)
        
        # add spaces until reached max len after add | to finish the line, do -2 for the space and |
        while len(line) < asciiEnemies.DESCRIPTIONLEN - 2:
            line += " "
        line += "|\n"

        # append each line to the lines list and clear line
        lines.append(line)
        line = ""
    
    return "".join(lines)

# no tests because ASCII art


# formatDescriptionList([string]) -> string
# purpose: formats a list of description strings from input (descriptionList) 
#          into a single string for ascii enemies. 
def formatDescriptionList(descriptionList):
    totalDescriptions = []
    # loop through the descrption lists and append
    for description in descriptionList:
        totalDescriptions.append(formatDescription(description))
    # has to do total descriptions twice each times
    if len(totalDescriptions) < 2:
        totalDescriptions.append(formatDescription(" "))
    # join total description list into a string with a next line so its seperated
    return "\n".join(totalDescriptions)

# no tests because ASCII art