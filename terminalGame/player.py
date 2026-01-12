import helperFuncs
import random
import time
from regularMode import regularPlayer
from enemyIntentions import intentionsList
from cardDefinitions import cardDef
import enemyHelpers
import inventory

# game constants
COST_GAIN = 3
STARTING_DRAW = 5
HAND_MAX = 14
PLAYER_HEALTH_MAX = 50
DIFFICULTY_MODIFIER = 0.5

# game
playerHealth = 50
costMax = 4
cost = 0
playerBlock = 0
difficulty = float(0.5)
combatDifficulty = 0
turnNumber = 0
roll = []
visibleIntentions = {}
discard = []
hand = []
deck = []
enemies = dict({})

# compatability mode
compatability = True

def compSleep(seconds):
    global compatability
    if compatability:
        time.sleep(seconds)

# resolveIntentions([str]) -> None
# purpose: takes in a list called resolveList, then executes all strings within the list as functions associated with it's name.
# examples:
#           resolveIntentions("damagePlayer(1,2)")                        -> playerHealth - 2
#           resolveIntentions("discardCardRand(2)")                       -> len(hand) - 2
#           resolveIntentions(["damagePlayer(2,2)", "damagePlayer(1,5)"]) -> playerHealth - 7
def resolveIntentions(resolveList):
    global intentionsList
    global roll
    healthList = {}
    print(resolveList)
    # Main loop for each enemies attack
    for i in range(len(list(resolveList.keys()))):
        # Health viewing for compatability
        for j in enemies:
            healthList[j] = enemies[j]["health"]
        # printing information for compatability
        helperFuncs.clearTerminal()
        compPrint(healthList)
        compPrint(resolveList[i+1]["description"])
        compPrint(f"roll: {roll}")
        #  shows block if it is above 0
        if playerBlock > 0:
            compPrint(playerBlock)
        compPrint(playerHealth)
        compSleep(0.5)
        # executes the function associated with the effect
        exec(resolveList[i+1]["effect"])
    # printing updated information
    helperFuncs.clearTerminal()
    compPrint(healthList)
    compPrint(resolveList[i+1]["description"])
    compPrint(f"roll: {roll}")
    if playerBlock > 0:
        compPrint(playerBlock)
    compPrint(playerHealth)

def deckDiscard(number):
    global deck
    global discard
    for i in range(number):
        try:
            card = random.randint(0,len(deck) - 1)
            deck.remove(card)
            discard.append(card)
        except:
            pass

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
            # get card is true for is discarding
            discarding = getCard("Card to discard: ", True)
            if discarding in hand:
                discardCard(discarding)
                cost += 1
                i += 1
            else:
                i += 1
                time.sleep(1)
            helperFuncs.clearTerminal()
    except:
        pass

# ammoCard(str,int,int,str) -> None
# purpose: takes in multiple strings and integers called card, times, damage, and effect. It then performs an action based off effect, using
#           times and damage, before replacing itself with the related reload card.
def ammoCard(card,times,damage,effect):
    # determining what happens
    match effect:
        case "single":
            damageEnemy(times,damage)
        case "recursion":
            damageEnemy(times,damage)
            chanceCheck = random.randint(1,2)
            # replaying loop
            while chanceCheck == 2 and enemies != {}:
                damageEnemy(times,damage)
                chanceCheck = random.randint(1,2)
        case "all":
            damageEnemyRand(times, helperFuncs.diceRoll(1, damage))
    # replaces card with the reload card
    discard.remove(card)
    deck.append(card+"-reload")

def damageEnemyRand(times,number):
    global enemies
    global roll
    global visibleIntentions
    roll = []
    helperFuncs.clearTerminal()
    enemyList = list(enemies.keys())
    for i in range(times):
        enemies[enemyList[random.randint(0,len(enemyList)-1)]]["health"] -= number
        roll.append(number)
        checkEnemyHealth()
def checkEnemyHealth():
    enemyList = list(enemies.keys())
    for i in range(len(enemyList)):
        if enemies[enemyList[i]]["health"] <= 0:
            enemies.pop(enemyList[i])
            visibleIntentions.pop(enemyList[i])

def reloadCard(card,times):
    global deck
    global discard
    cardsRemoved = 0
    i = 0
    match card:
        case "blunderbuss":
            damageEnemyAll(1,16)

    if times == 1:
        deck.append(card)
        discard.remove(card+"-reload")
    else:
        while (i < len(deck)) and (cardsRemoved <= times):
            card = deck[i]
            if "-reload" in card:
                    deck.append(card[:-7])
                    deck.remove(card)
                    cardsRemoved += 1
            i += 1
        

def damageEnemyAll(times,number):
    global enemies
    global roll
    global visibleIntentions
    roll = []
    helperFuncs.clearTerminal()
    enemyList = list(enemies.keys())
    for i in range(len(enemyList)):
        for e in range(times):
            enemies[enemyList[i]]["health"] -= number
            roll.append(number)
            visibleIntentions = enemyHelpers.updateEnemyHealth(visibleIntentions,enemies)
            checkEnemyHealth()

# enemyDamageSelf(int,int) -> None
# purpose: takes in two integers called times and number, and reduces the enemies health by number x times.
def enemyDamageSelf(times,number):
    global enemies
    global visibleIntentions
    for i in range(times):
        addEnemy = random.choice(list(enemies.keys()))
        enemies[addEnemy]["health"] -= number
        enemyHelpers.updateEnemyHealth(visibleIntentions,enemies)
        checkEnemyHealth()

# Not used for non-compatability mode
# defineCard() -> None
# purpose: runs a sequence to print the description of cards in compatability mode.
# def defineCard():
#     global cardDef
#     print(hand)
#     cardInput = input("Which Card: ")
#     try:
#         print(cardDef[cardInput]["description"])
#     except:
#         print("Invalid Card")
#     time.sleep(2)


# damagePlayer(int,int) -> None
# purpose: Takes in two integers called times and number, and decreases the player health by number * times - block.
# examples:
#           damagePlayer(1,2) -> playerHealth - 2
#           damagePlayer(4,1) -> playerHealth - 4
#           damagePlayer(2,2) -> playerHealth - 4
def damagePlayer(times,number):
    global playerHealth
    global playerBlock
    global roll
    finalNumber = number
    roll = []
    for i in range(times):
        roll.append(number)
        if playerBlock > 0:
            finalNumber = number - playerBlock
            playerBlock -= number
        if finalNumber > 0:
            playerHealth -= finalNumber


def getEnemy(string):
    global compatability
    global hand
    target = ""
    # determines to use input or function
    if compatability:
        target = input(string)
    else:
        target = regularPlayer.getEnemySelected()
    return target

def getCard(string, isDiscarding):
    global compatability
    global hand
    target = ""
    # determines to use input or function
    if compatability:
        target = input(string)
    else:
        target = regularPlayer.getCardSelected(hand, isDiscarding)
    return target

def compPrint(string):
    if compatability:
        print(string)

def damageEnemy(times,number):
    i = 0
    global enemies
    global visibleIntentions
    global roll
    while i < times:
        helperFuncs.clearTerminal()
        compPrint(list(enemies.keys()))
        target = getEnemy("Choose an enemy: ")
        try:
            enemies[target]["health"] -= number
            roll.append(number)
            enemyHelpers.updateEnemyHealth(visibleIntentions,enemies)
            i += 1
            if enemies[target]["health"] <= 0:
                enemies.pop(target)
                visibleIntentions.pop(target)
        except:

            compSleep(1)
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
    global deck
    global hand
    global discard
    global playerHealth
    global inventory
    global visibleIntentions
    deck = inventory.cards.copy()
    hand = []
    discard = []
    playerHealth = PLAYER_HEALTH_MAX
    setup = enemyHelpers.determineIntentions(enemyHelpers.determineEnemies(enemies,difficulty), turnNumber)
    enemies = setup[0]
    visibleIntentions = setup[1]
    helperFuncs.clearTerminal()
    print("START COMBAT")
    time.sleep(1)

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
    drawCards(STARTING_DRAW)
    cost += COST_GAIN
    playerBlock = 0
    helperFuncs.clearTerminal()
    compPrint("your turn")
    compSleep(1)
    while True:
        helperFuncs.clearTerminal()
        turnNumber += 1
        while len(hand) > HAND_MAX:
            hand.pop()
        while cost > costMax:
            cost -= 1
        compPrint(f"hand: {hand}")
        compPrint(f"discard: {discard}")
        compPrint(f"deck: {deck}")
        compPrint(f"cost: {cost}")
        compPrint(f"health: {playerHealth}")
        compPrint(f"block: {playerBlock}")
        compPrint(visibleIntentions)
        if enemies == {}:
            return
        # takes string false for is not discarding
        playCard = getCard("", False).lower()
        try:
            effect = cardDef[playCard]["effect"]
        except:

                compSleep(1)
        else:
            currentCardCost = cardDef[playCard]["cost"]
            if (playCard in hand):
                if cost - currentCardCost > -1:
                    helperFuncs.clearTerminal()
                    discardCard(playCard)
                    cost -= currentCardCost
                    exec(effect)
                    
                else:
                    compPrint("Invalid Card")
                    compSleep(1)
            elif playCard == "define":
                helperFuncs.clearTerminal()
                exec(effect)
            elif playCard == "end":
                compSleep(1)
                helperFuncs.clearTerminal()
                discardCardRand(len(hand))
                return
            else:
                compPrint("Invalid Card")
                compSleep(1)
def enemyTurn():
    global playerHealth
    global enemies
    global turnNumber
    global visibleIntentions
    enemyList = list(enemies.keys())
    for i in range(len(list(enemies.keys()))):

        resolveIntentions(enemies[enemyList[i]]["attacks"])
    # Determine next enemies attack
    visibleIntentions = enemyHelpers.determineIntentions(enemies, turnNumber)[1]

def gameLoop(isCompatabilityMode):
    # set compatability
    global compatability
    compatability = isCompatabilityMode

    # set victory and start combat
    won = True
    startCombat()
    # loop until our or all the enemies died
    while enemies != {} and playerHealth > 0:
        playerTurn()
        enemyTurn()
    # if your health is below 0 you lost
    if playerHealth <= 0:
        won = False
        
    return won
