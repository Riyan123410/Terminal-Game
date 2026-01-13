# main() -> "mainMenu"
# purpose: main function for how to play, prints the credits and waits
#          until the user enters anything in the console to which it would always return 
#          "mainMenu" for the next game state
def main():

    # print reminder
    print("REMEMBER TO SCROLL TO TOP WHEN HOW TO PLAY IS DISPLAYED\n[ENTER] to continue")
    input()

    # print how to play essay(shorter than header comments to be honest)
    print(r"""                                   
 _                _              _         
| |_ ___ _ _ _   | |_ ___    ___| |___ _ _ 
|   | . | | | |  |  _| . |  | . | | .'| | |
|_|_|___|_____|  |_| |___|  |  _|_|__,|_  |
                            |_|       |___|

BASICS:
    [W,A,S,D] to move your selection
    [space] to select
    [ENTER to continue]

>> when pressing play you will be prompted with PLAY and SHOP
SHOP:
    you can select to purchase a card with coins, coins are
    displayed on bottom left
    
    you will enter a screen that will look like this:
    [card][card][card][card][back]
    ==============================
    [coins]

    W,D to move around space to select

PLAY:
>> select card:
    you will enter a screen that looks like this:

    [ENEMY]
    [DECK] [DISCARD] [END TURN]
    [------------CARDS------------]
    ===============================
    [HP] [BLOCK] [COST]

    you can press space to use a card, your cost are displayed on
    bottom left that you spend to play cards, with health and block*

>> discard card:
    you will enter the same screen as before however under the =
    line it will say discard a card, this will happen after you 
    play a card that says discard cards. Simply select the
    card to discard it, you may be prompted to discard
    multiple cards.

>> attack enemy
    you will enter a screen that looks like this:

    [ENEMY][ENEMY][ENEMY]
      /|\
       |
    
    you can use A,D to select an enemy and space to attack the enemy
    you may be prompted to attack multiple enemies

In order to view the deck, discard or end your turn, press W,S to go
up and down and space to select that action

DEFINITIONS:

    [BLOCK] block will just subtract damage that is done to you.
            no, block cannot heal if its higher than damage:
            DAMAGE DONE = DAMAGE - BLOCK

    [COST] each card has a cost listed in the top right. 
           Default cost you gain each turn is 3. If you
           dont have enough you can't use the card

    [COINS] used to buy cards in the shop
          
    [AMMO] when played, replaces the card with a 'reload' card,
           which requires to be played again for the main card
           to be re-added
          
    [EXERT] removes itself from the current round when played
          
    [PERMANENT] applies a permanent effect to you, which
                carries over between rounds

    [POWER] increases damage done by X, where X is equal to
            the current amount of power

    [HASTE] gain 1 card when you play a card

    [ENERGETIC] gain 1 cost when you play a card


if you're still confused i wasted my time ):

SCROLL TO TOP AND READ TOP TO BOTTOM
[ENTER] to go back
""")
    # wait for input than return main menu
    input()
    return "mainMenu"