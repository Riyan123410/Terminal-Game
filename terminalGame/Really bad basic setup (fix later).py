import helperFuncs
import random
import time



playerHealth = 50
costMax = 4
cost = 0
playerBlock = 0
costGain = 3
enemyHealth = 40
startingDraw = 4
turnNumber = 0
ply = 0
visibleIntentions = []
handMax = 15
discard = []
hand = []
cardDef = {"end" : ["passes turn", "endTurn()", 0], "define" : ["defines",  "defineCard()", 0], "strike" : ["deals 4 damage, 1 target", "damageEnemy(1,4)", 1], "block" : ["gain 3 block", "gainBlock(1,3)", 1], "clean sweep" : ["discard 2 cards, then gain 2 cost", "discardGain(2)", 0]}
deck = ["strike", "clean sweep", "strike", "strike", "strike", "strike", "strike", "strike", "strike", "block", "block", "block"]
enemies = {"goose" : []}
intentionsList = {"goose" : {"turn1" : {"attackTimes" : 2, 1 : {"description" : "deal 2d4 damage", "effect" : "damagePlayer(1,diceRoll(2,4))"}, 2 : {"description" : "Discard 1 card from your hand", "effect" : "discardCardRand(1)"}}, "turn2" : {"attackTimes" : 2, 1 : {"description" : "deal 2d4 damage", "effect" : "damagePlayer(1,diceRoll(2,4))"}, 2 : {"description" : "Discard 1 card from your hand", "effect" : "discardCardRand(1)"}}}}


def resolveIntentions(list):
    global intentionsList
    global ply
    for i in list:
        exec(i["effect"])
def determinePly():
    global ply
    global turnNumber
    if turnNumber % 2 == 0:
        ply = 1
        return "turn1"
    else:
        ply = 0
        return "turn2"
def diceRoll(times,size):
    roll = 0
    for i in range(times):
        roll += random.randint(1,size)
    return roll
def enemyIntentions(enemyName):
    global intentionsList
    attackIntentions = []
    for i in range(intentionsList[enemyName][determinePly()]["attackTimes"]):
        attackIntentions.append(intentionsList[enemyName][determinePly()][i+1])
    return attackIntentions

def determineIntentions():
    global enemies
    global visibleIntentions
    global intentionsList
    visibleIntentions = []
    enemyList = list(enemies.keys())
    print(enemyList)
    for i in range(len(enemyList)):
        enemies[enemyList[i]] = enemyIntentions(enemyList[i])
        print(enemies[enemyList[i]])
        for e in range(intentionsList[enemyList[i]][determinePly()]["attackTimes"]):

            visibleIntentions.append(enemies[enemyList[i]][e]["description"])
def discardGain(number):
    global hand
    for i in range(number):
        print(hand)
        discarding = input("Card to discard: ")
        global cost
        try:
            discardCard(discarding)
        except:
            print("Invalid Card")
            print(i)
            i -= 1
            time.sleep(1)
        else:
            cost += 1
        helperFuncs.clearTerminal()
def defineCard():
    cardInput = input("Which Card: ")
    global cardDef
    print(cardDef[cardInput][0])
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
        cardToDiscard = (hand[random.randint(0,len(hand) - 1)])
        discard.append(cardToDiscard)
        hand.remove(cardToDiscard) 
def discardCard(name):
    global discard
    global hand
    discard.append(name)
    hand.remove(name)
determineIntentions()
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
        print(enemyHealth)
        print(f"discard: {discard}")
        print(f"deck: {deck}")
        print(f"cost: {cost}")
        print(f"player health: {playerHealth}")
        print(visibleIntentions)
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
    global ply
    global visibleIntentions
    enemyList = list(enemies.keys())
    determinePly()
    for i in range(len(enemies)):
        print(enemies[enemyList[i]])
        resolveIntentions(enemies[enemyList[i]])
    # Determine next enemies attack
    determineIntentions()
while True:
    playerTurn()
    enemyTurn()