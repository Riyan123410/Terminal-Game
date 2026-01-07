import random
import helperFuncs
import time

cardDef = {"end" : ["passes turn", "print('how are you seeing this')", 0], "define" : ["defines",  "defineCard()", 0], "strike" : ["deals 4 damage, 1 target", "damageEnemy(1,4)", 1], "block" : ["gain 3 block", "gainBlock(1,3)", 1], "clean sweep" : ["discard 2 cards, then gain 2 cost", "discardGain(2)", 0]}
playerHealth = 50
costMax = 4
cost = 0
block = 0
playerBlock = 0
costGain = 3
enemyHealth = 40
startingDraw = 4
turnNumber = 0
visibleIntentions = []
handMax = 15
deck = ["strike", "clean sweep", "strike", "strike", "strike", "strike", "strike", "strike", "strike", "block", "block", "block"]
hand = []
discard = []
cost = 0
deck = []

def discardGain(number):
    global hand
    global cost
    i = 0
    while (i < number) or (hand > 0):
        print(hand)
        discarding = input("Card to discard: ")
        if discarding in hand:
            discardCard(discarding)
            cost += 1
            i += 1
        else:
            print("Invalid Card")
            time.sleep(1)
        helperFuncs.clearTerminal()
def defineCard():
    global cardDef
    print(hand)
    cardInput = input("Which Card: ")
    try:
        print(cardDef[cardInput][0])
    except:
        print("Invalid Card")
    time.sleep(2)
def damagePlayer(times,number):
    global playerHealth
    for i in range(times):
        playerHealth -= number
def damageEnemy(times,number):
    global enemyHealth
    for i in range(times):
        enemyHealth -= number
def gainBlock(times,number):
    global playerBlock
    for i in range(times):
        playerBlock += number
def drawCards(number):
    global discard
    global hand
    global deck
    if len(deck) == 0:
            deck = discard.copy()
            discard.clear()
    for i in range(number):
        try:
            selectedCard = deck[random.randint(0, len(deck) - 1)]
            hand.append(selectedCard)
            deck.remove(selectedCard)
        except:
            pass

def discardCardRand(number):
    global discard
    global hand
    cardToDiscard = ""
    for i in range(number):
        try:
            cardToDiscard = (hand[random.randint(0,len(hand) - 1)])
            discard.append(cardToDiscard)
            hand.remove(cardToDiscard)
        except:
            pass
def discardCard(name):
    global discard
    global hand
    discard.append(name)
    hand.remove(name)