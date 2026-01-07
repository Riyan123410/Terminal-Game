import helperFuncs
import random
import time
from enemyIntentions import intentionsList
from cardDefinitions import cardDef
import enemyHelpers



playerHealth = 50
costMax = 4
cost = 0
playerBlock = 0
difficulty = 2
combatDifficulty = 0
costGain = 3
enemyHealth = 40
startingDraw = 4
turnNumber = 0
visibleIntentions = {}
handMax = 14
discard = []
hand = []
deck = ["strike", "clean sweep", "strike", "strike", "strike", "strike", "strike", "strike", "strike", "block", "block", "block"]
enemies = dict({})

def resolveIntentions(list):
    global intentionsList
    for i in list:
        exec(i["effect"])

def checkDeck():
    global deck
    print(deck)
    time.sleep(2)


def discardGain(number):
    global hand
    global cost
    i = 0
    while (i < number):
        print(hand)
        discarding = input("Card to discard: ")
        if discarding in hand:
            discardCard(discarding)
            cost += 1
            i += 1
        else:
            print("Invalid Card")
            i += 1
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
    global enemies
    helperFuncs.clearTerminal()
    print(list(enemies.keys()))
    target = input("Which enemy: ")
    for i in range(times):
        enemies[target]["health"] -= number
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


def startCombat():
    global enemies
    global turnNumber
    global visibleIntentions
    setup = enemyHelpers.determineIntentions(enemyHelpers.determineEnemies(enemies,difficulty), turnNumber)
    enemies = setup[0]
    visibleIntentions = setup[1]

def playerTurn():
    global cost
    global hand
    global block
    global playerHealth
    global costMax
    global enemyHealth
    global cardDef
    global turnNumber
    drawCards(startingDraw)
    cost += costGain
    block = 0
    helperFuncs.clearTerminal()
    print("your turn")
    time.sleep(1)
    while True:
        helperFuncs.clearTerminal()
        turnNumber += 1
        while len(hand) > handMax:
            hand.pop()
        while cost > costMax:
            cost -= 1
        print(f"hand: {hand}")
        print(f"enemy health: {enemyHealth}")
        print(f"discard: {discard}")
        print(f"deck: {deck}")
        print(f"cost: {cost}")
        print(f"player health: {playerHealth}")
        print(visibleIntentions)
        print(enemies)
        playCard = input().lower()
        try:
            effect = cardDef[playCard][1]
        except:
                print("Invalid Card")
                time.sleep(1)
        else:
            currentCardCost = cardDef[playCard][2]
            if (playCard in hand):
                if cost - currentCardCost > -1:
                    helperFuncs.clearTerminal()
                    discardCard(playCard)
                    cost -= currentCardCost
                    exec(effect)
                    
                else:
                    print("Not enough cost")
                    time.sleep(1)
            elif playCard == "define":
                helperFuncs.clearTerminal()
                exec(effect)
            elif playCard == "end":
                time.sleep(1)
                helperFuncs.clearTerminal()
                return
            else:
                print("Card not in hand")
                time.sleep(1)
def enemyTurn():
    global playerHealth
    global enemies
    global turnNumber
    global visibleIntentions
    enemyList = list(enemies.keys())
    for i in range(len(enemies)):
        print(enemies[enemyList[i]])
        resolveIntentions(enemies[enemyList[i]]["attacks"])
    # Determine next enemies attack
    enemyHelpers.determineIntentions(enemies, turnNumber)

def gameLoop():
    startCombat()
    while True:
        playerTurn()
        enemyTurn()
gameLoop()