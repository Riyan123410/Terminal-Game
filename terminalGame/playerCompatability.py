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
difficulty = 0.5
combatDifficulty = 0
costGain = 3
startingDraw = 5
turnNumber = 0
visibleIntentions = {}
handMax = 14
discard = []
hand = []
deck = ["strike", "clean sweep", "strike", "strike", "strike", "strike", "strike", "strike", "strike", "block", "block", "block", "crossbow", "well prepared"]
enemies = dict({})

# resolveIntentions([str]) -> None
# purpose: takes in a list called resolveList, then executes all strings within the list as functions associated with it's name.
# examples:
#           resolveIntentions("damagePlayer(1,2)")                        -> playerHealth - 2
#           resolveIntentions("discardCardRand(2)")                       -> len(hand) - 2
#           resolveIntentions(["damagePlayer(2,2)", "damagePlayer(1,5)"]) -> playerHealth - 7
def resolveIntentions(resolveList):
    global intentionsList
    healthList = {}
    for i in resolveList:
        for e in enemies:
            healthList[e] = enemies[e]["health"]
        helperFuncs.clearTerminal()
        print(healthList)
        print(i["description"])
        if playerBlock > 0:
            print(playerBlock)
        print(playerHealth)
        time.sleep(0.5)
        exec(i["effect"])
    helperFuncs.clearTerminal()
    print(healthList)
    print(i["description"])
    if playerBlock > 0:
        print(playerBlock)
    print(playerHealth)



# discardGain(int) -> None
# purpose: takes in an integer called number, then discards as many entrys from number from the hand, and increases cost by number discarded.
# examples:
#           discardGain(1) -> len(hand) - 1, len(discard) + 1, cost + 1
#           discardGain()  -> nothing
#           discardGain(4) -> len(hand) - 4, len(discard) + 4, cost + 4
def discardGain(number):
    global hand
    global cost
    i = 0
    try:
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
    except:
        pass

def enemyDamageSelf(times,number):
    global enemies
    global visibleIntentions
    for i in range(times):
        addEnemy = random.choice(list(enemies.keys()))
        enemies[addEnemy]["health"] -= number
        enemyHelpers.updateEnemyHealth(visibleIntentions,enemies)
        if enemies[addEnemy]["health"] <= 0:
                enemies.pop(addEnemy)
                visibleIntentions.pop(addEnemy)

# defineCard() -> None
# purpose: runs a sequence to print the description of cards in compatability mode.
def defineCard():
    global cardDef
    print(hand)
    cardInput = input("Which Card: ")
    try:
        print(cardDef[cardInput][0])
    except:
        print("Invalid Card")
    time.sleep(2)


# damagePlayer(int,int) -> None
# purpose: Takes in two integers called times and number, and decreases the player health by number * times - block.
# examples:
#           damagePlayer(1,2) -> playerHealth - 2
#           damagePlayer(4,1) -> playerHealth - 4
#           damagePlayer(2,2) -> playerHealth - 4
def damagePlayer(times,number):
    global playerHealth
    global playerBlock
    finalNumber = number
    for i in range(times):
        if playerBlock > 0:
            finalNumber = number - playerBlock
            playerBlock -= number
        if finalNumber > 0:
            playerHealth -= finalNumber


def damageEnemy(times,number):
    i = 0
    global enemies
    global visibleIntentions
    while i < times:
        helperFuncs.clearTerminal()
        print(list(enemies.keys()))
        target = input("Which enemy: ")
        try:
            enemies[target]["health"] -= number
            enemyHelpers.updateEnemyHealth(visibleIntentions,enemies)
            i += 1
            if enemies[target]["health"] <= 0:
                enemies.pop(target)
                visibleIntentions.pop(target)
        except:
            print("Invalid Enemy")
            time.sleep(1)
def gainBlock(times,number):
    global playerBlock
    for i in range(times):
        playerBlock += number

# drawCards(int) -> None
# purpose: takes in an integer called number, and adds cards from the deck to the hand.
# examples:
#           drawCards(1) -> len(hand) + 1, len(deck) - 1
#           drawCards(2) -> len(hand) + 2, len(deck) - 1
def drawCards(number):
    global discard
    global hand
    global deck
    for i in range(number):
        try:
            if len(deck) == 0:
                deck = discard.copy()
                discard.clear()
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

# discardCard(str) -> None
# purpose: takes in a string called name, then removes a card in your hand with the same name, and adds it to the discard.
# examples:
#           discardCard("strike")      -> len(hand) - 1, len(discard) + 1
#           discardCard("clean sweep") -> len(hand) - 1, len(discard) + 1
def discardCard(name):
    global discard
    global hand
    discard.append(name)
    hand.remove(name)

# startCombat() -> None
# purpose: initializes a combat encounter by determining enemies, the intentions, and health.
def startCombat():
    global enemies
    global turnNumber
    global visibleIntentions
    setup = enemyHelpers.determineIntentions(enemyHelpers.determineEnemies(enemies,difficulty), turnNumber)
    enemies = setup[0]
    visibleIntentions = setup[1]

# playerTurn() -> None
# purpose: starts the players turn, and starts taking their actions
def playerTurn():
    global cost
    global hand
    global playerBlock
    global playerHealth
    global costMax
    global cardDef
    global turnNumber
    drawCards(startingDraw)
    cost += costGain
    playerBlock = 0
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
        print(f"discard: {discard}")
        print(f"deck: {deck}")
        print(f"cost: {cost}")
        print(f"health: {playerHealth}")
        print(f"block: {playerBlock}")
        print(visibleIntentions)
        if enemies == {}:
            return
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
                discardCardRand(len(hand))
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
    visibleIntentions = enemyHelpers.determineIntentions(enemies, turnNumber)[1]

def gameLoopCompatable():
    startCombat()
    while enemies != {}:
        playerTurn()
        enemyTurn()