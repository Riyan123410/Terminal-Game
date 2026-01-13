from asciiArt import asciiHelpers
from asciiArt import asciiMenus
import helperFuncs
import userInput
import random
import inventory

# shop variables

# prices are based on damage per cost, if applicable
# multiplied by 2 since you gain coins exponentally
itemCoins = {
    "soldOut" : 0,
    "strike" : 4 * 2,
    "block" : 1 * 2,
    "clean sweep" : 4 * 2,
    "crossbow" : 6 * 2,
    "well prepared" : 4 * 2,
    "blunderbuss" : 7 * 2,
    "revolver" : 6 * 2,
    "cannon" : 12 * 2,
    "multi-strike" : 12 * 2,
    "organ gun" : 5 * 2,
    "tactical reload" : 2 * 2,
    "super block" : 3 * 2,
    "sonic speed" : 3 * 2,
    "supressive fire" : 1 * 2
}
currentStock = []

# menu constants
MENUMAX = 5
MENUMIN = 1
MENUDIR = "xDir"


# listToBookshelf([str]) -> [str]
# purpose: converts a list of stock items from the parameter list [currentStock] 
#          into their ASCII art cards and appends the back slot at the end
def listToBookshelf(currentStock):
    # create empty bookshelf list
    bookshelfList = []

    # loop through the current stock appenging to the list and than retun it
    for item in currentStock:
        bookshelfList.append(asciiMenus.shop["cards"][item])
    
    # append the back button and returns the bookshelf
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
    indexToArrow = asciiHelpers.indexToArrow(currentSelected, MENUMAX, asciiMenus.shop["select"]["blank"], asciiMenus.shop["select"]["arrow"], asciiMenus.shop["select"]["lastArrow"])
    arrow = asciiHelpers.combineCardStrings(indexToArrow, asciiMenus.shop["select"]["height"])
    controls = asciiMenus.getCoinMenuControls(coins)
    info = f"Current deck: {cards}"
    # add all ascii and return the full art
    return  bookShelf + arrow + controls + info


# resetStock() -> None
# purpose: resets the global shop stock by clearing the currentStock list
#          and filling it with randomly selected items from the itemCoins list
#          based on the MENUMAX constant
def resetStock():
    # use global current stock and reset it
    global currentStock
    currentStock = []

    # create shop items by making it  into a list so a random index can be chosen
    itemsList = list(itemCoins)
    for i in range(MENUMAX - 1):
        currentStock.append(random.choice(itemsList))

# main() -> str
# purpose: runs the shop interface, handles input and purchases, 
#          updates inventory, and always returns "playMenu" when the
#          back button is pressed
def main():
    # use global current stock and reset it, set coins based on current inventory
    global currentStock
    coins = inventory.coins

    # set current selected and clear terminal to print shop
    currentSelected = MENUMIN
    helperFuncs.clearTerminal()

    # get cards and print the shop
    cards = inventory.cards
    print(getArt(currentSelected, coins, cards))
    
    # loop
    while True:
        # get input and change with clamp
        inputList = userInput.getInputList()
        currentSelected = helperFuncs.changeWithClamp(currentSelected, inputList[MENUDIR], MENUMIN, MENUMAX)

        # check if space is pressed so an action can be done
        if inputList["space"] == True:
            
            # if its the last item in the list return main menu to go there, if not purchase an item if you have enough coins
            if currentSelected == MENUMAX:
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

# run reset stock when game begins
resetStock()