from asciiArt import asciiHelpers
from asciiArt import asciiMenus
import helperFuncs
import userInput
import os
import random

# shop variables
itemCoins = {
    "strike" : 1,
    "soldOut" : 0
}
currentStock = []

# menu constants
MENU_MAX = 5
MENU_MIN = 1
MENU_DIR = "xDir"
currentSelected = MENU_MIN

# shop constants
MAX_CARDS = 7

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

    # use global current stock and reset it
    global currentStock
    currentStock = []
    # create shop items by making it  into a list so a random index can be chosen
    itemsList = list(itemCoins)
    for i in range(MENU_MAX - 1):
        currentStock.append(random.choice(itemsList))

    # get coins
    coins = helperFuncs.getCoins()

    # open the save file where your coins can be saved 
    saveFile = open("save.txt", "r")
    saveFile.seek(0)
    # read the data from the save file and close it
    cards = saveFile.readlines()
    saveFile.close()

    # set current selected and clear terminal to print shop
    currentSelected = MENU_MIN
    helperFuncs.clearTerminal()
    print(getArt(currentSelected, coins, cards))
    
    # loop
    while True:
        # get input and change with clamp
        inputList = userInput.getInputList()
        currentSelected = helperFuncs.changeWithClamp(currentSelected, inputList[MENU_DIR], MENU_MIN, MENU_MAX)

        # check if space is pressed so an action can be done
        if inputList["space"] == True:
            
            # if its the last item in the list return main menu to go there, if not purchase an item if you have enough coins
            if currentSelected == MENU_MAX:
                saveCardsAndCoins(cards, coins)
                return "playMenu"

            # get price of item so it can be used later, subtract 1 because current selected is 1-5 while list is 0-4
            itemPrice = itemCoins[currentStock[currentSelected - 1]]

            # check if you can buy the item
            if coins >= itemPrice and currentStock[currentSelected - 1] != "soldOut" and len(cards) < MAX_CARDS:
                # subtrace coins and append the cards list based on what you bought with \n so its on another lin
                coins -= itemPrice
                cards.append(currentStock[currentSelected - 1] + "\n")
                # set the item to sold out
                currentStock[currentSelected - 1] = "soldOut"
        
        # create arrow
        helperFuncs.clearTerminal()
        print(getArt(currentSelected, coins, cards))

def getArt(currentSelected, coins, cards):
    # get each asii art of the shop from menus and return it
    bookShelf = asciiHelpers.combineCardStrings(listToBookshelf(currentStock), asciiMenus.shop["bookshelfHeight"])
    arrow = asciiHelpers.combineCardStrings(indexToArrow(currentSelected), asciiMenus.shop["select"]["height"])
    controls = asciiMenus.getCoinMenuControls(coins)
    info = f"Warning! purchased items will not be saved until you press back\n Current deck: {helperFuncs.removeEndlinesInList(cards)}"
    if len(cards) >= MAX_CARDS:
        info = f"Warning! purchased items will not be saved until you press back\n Cannot purchase cards - deck cap reached of {MAX_CARDS}"
    return  bookShelf + arrow + controls + info

def saveCardsAndCoins(cards, coins):
    # open file in write mode, set the index to coins with \n so its another line and write the file
    saveFile = open("save.txt", "w")
    cards[0] = str(coins) + "\n"
    saveFile.writelines(cards)

    # close file as its done being used
    saveFile.close()
    