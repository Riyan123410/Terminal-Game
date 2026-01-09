from asciiArt import asciiHelpers
from asciiArt import asciiMenus
import helperFuncs
import userInput
import os

itemCoins = {
    "strike" : 1,
    "block" : 1
}
currentStock = ["strike", "strike", "strike", "strike"]

MENU_MAX = 5
MENU_MIN = 1
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
    if currentSelected == MENU_MAX:
        arrowList.append(asciiMenus.shop["select"]["lastArrow"])
    else:
        arrowList.append(asciiMenus.shop["select"]["arrow"])
    return arrowList

def main():
    # get coins
    coins = helperFuncs.getCoins()

    # set current selected and clear terminal to print shop
    currentSelected = MENU_MIN
    helperFuncs.clearTerminal()
    print(getArt(currentSelected, coins))
    
    # open the save file where your coins can be saved 
    saveFile = open("save.txt", "r")
    saveFile.seek(0)
    # read the data from the save file and close it
    cards = saveFile.readlines()
    saveFile.close()
    
    # loop
    while True:
        # get input and change with clamp
        inputList = userInput.getInputList()
        currentSelected = helperFuncs.changeWithClamp(currentSelected, inputList[MENU_DIR], MENU_MIN, MENU_MAX)

        # create arrow
        helperFuncs.clearTerminal()
        print(getArt(currentSelected, coins))

        # check if space is pressed so an action can be done
        if inputList["space"] == True:
            # get price of item so it can be used later, subtract 2 because 1 for the back button
            # the other is because items start at 1 not 0
            itemPrice = itemCoins[currentStock[currentSelected - 2]]
            # if its the last item in the list return main menu to go there, if not purchase an item if you have enough coins
            if currentSelected == MENU_MAX:
                saveCardsAndCoins(cards, coins)
                return "playMenu"
            elif coins >= itemPrice:
                # subtrace coins and append the cards list based on what you bought with \n so its on another lin
                coins -= itemPrice
                cards.append(currentStock[currentSelected - 2] + "\n")
            else:
                print("Not enough coins")

def getArt(currentSelected, coins):
    # get each asii art of the shop from menus and return it
    bookShelf = asciiHelpers.combineCardStrings(listToBookshelf(currentStock), asciiMenus.shop["bookshelfHeight"])
    arrow = asciiHelpers.combineCardStrings(indexToArrow(currentSelected), asciiMenus.shop["select"]["height"])
    controls = asciiMenus.getCoinMenuControls(coins)
    saveWarning = "Warning! purchased items will not be saved until you press back"
    return  bookShelf + arrow + controls + saveWarning

def saveCardsAndCoins(cards, coins):
    # open file in write mode, set the index to coins with \n so its another line and write the file
    saveFile = open("save.txt", "w")
    cards[0] = str(coins) + "\n"
    saveFile.writelines(cards)

    # close file as its done being used
    saveFile.close()