from asciiArt import asciiHelpers
from asciiArt import asciiMenus
import helperFuncs
import userInput
import os
import random
import inventory

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


# listToBookshelf([str]) -> [str]
# purpose: converts a list of stock items from the parameter list [currentStock] 
#          into their ASCII art cards and appends the back slot at the end
def listToBookshelf(currentStock):
    # create empty bookshelf list
    bookshelfList = []
    # loop through the current stock appenging to the list and than retun it
    for item in currentStock:
        bookshelfList.append(asciiMenus.shop["cards"][item])
    bookshelfList.append(asciiMenus.shop["backSlot"])
    return bookshelfList


# getArt(int, int, [str]) -> str
# purpose: generates the full ASCII shop display including bookshelf, selection arrow,
#          coin display, and deck info based on current selection parmeter (currentSelected)
#          and the cards with the parameter (cards) it also prints the coins with the parameter
#          (coins)
def getArt(currentSelected, coins, cards):
    # get each asii art of the shop from menus and return it
    bookShelf = asciiHelpers.combineCardStrings(listToBookshelf(currentStock), asciiMenus.shop["bookshelfHeight"])
    indexToArrow = asciiHelpers.indexToArrow(currentSelected, MENU_MAX, asciiMenus.shop["select"]["blank"], asciiMenus.shop["select"]["arrow"], asciiMenus.shop["select"]["lastArrow"])
    arrow = asciiHelpers.combineCardStrings(indexToArrow, asciiMenus.shop["select"]["height"])
    controls = asciiMenus.getCoinMenuControls(coins)
    info = f"Current deck: {cards}"
    return  bookShelf + arrow + controls + info


# main() -> str
# purpose: runs the shop interface, handles input and purchases, 
#          updates inventory, and always returns "playMenu" when the
#          back button is pressed
def main():
    # use global current stock and reset it
    global currentStock
    currentStock = []
    # create shop items by making it  into a list so a random index can be chosen
    itemsList = list(itemCoins)
    for i in range(MENU_MAX - 1):
        currentStock.append(random.choice(itemsList))

    # get coins
    coins = inventory.coins

    # set current selected and clear terminal to print shop
    currentSelected = MENU_MIN
    helperFuncs.clearTerminal()
    cards = inventory.cards
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
                inventory.coins = coins
                return "playMenu"

            # get price of item so it can be used later, subtract 1 because current selected is 1-5 while list is 0-4
            itemPrice = itemCoins[currentStock[currentSelected - 1]]

            # check if you can buy the item
            if coins >= itemPrice and currentStock[currentSelected - 1] != "soldOut":
                # subtrace coins and append the cards list based on what you bought
                coins -= itemPrice
                cards.append(currentStock[currentSelected - 1])
                # set the item to sold out
                currentStock[currentSelected - 1] = "soldOut"
        
        # create arrow
        helperFuncs.clearTerminal()
        print(getArt(currentSelected, coins, cards))