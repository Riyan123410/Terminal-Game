from asciiArt import asciiHelpers
from asciiArt import asciiMenus
import helperFuncs
import userInput

items = ("strike")
currentStock = ["strike", "strike", "strike", "strike"]

MENU_MAX = 5
MENU_MIN = 0
MENU_DIR = "xDir"
currentSelected = MENU_MIN

def listToBookshelf(currentStock):
    # create empty bookshelf list
    bookshelfList = []
    # loop through the current stock appenging to the list and than retun it
    for item in currentStock:
        bookshelfList.append(asciiMenus.shop["cards"][item])
    bookshelfList.append(asciiMenus.shop["backSlot"])
    return bookshelfList

def indexToArrow(currentSelected):
    # create empty list
    arrowList = []
    # based on index subtract one to make a space for the arrow
    for i in range(currentSelected - 1):
        arrowList.append(asciiMenus.shop["select"]["blank"])
    # add the arrow and return the list
    arrowList.append(asciiMenus.shop["select"]["arrow"])
    return arrowList

def main():
    # set current selected and clear terminal to print shop
    currentSelected = MENU_MIN
    helperFuncs.clearTerminal()
    print(asciiHelpers.combineCardStrings(listToBookshelf(currentStock), asciiMenus.shop["bookshelfHeight"]))

    # loop
    while True:
        # get input and change with clamp
        inputList = userInput.getInputList()
        currentSelected = helperFuncs.changeWithClamp(currentSelected, inputList[MENU_DIR], MENU_MIN, MENU_MAX)

        # create arrow
        createArrow(currentSelected)

        # if space and last option leave
        if inputList["space"] == True:
            if currentSelected == MENU_MAX:
                return "playMenu"

def createArrow(currentSelected):
    helperFuncs.clearTerminal()
    print(asciiHelpers.combineCardStrings(listToBookshelf(currentStock), asciiMenus.shop["bookshelfHeight"]))
    print(asciiHelpers.combineCardStrings(indexToArrow(currentSelected), asciiMenus.shop["select"]["height"]))