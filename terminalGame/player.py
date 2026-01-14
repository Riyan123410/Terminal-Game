import helperFuncs
import random
import time
from regularMode import regularPlayer
from enemyIntentions import intentionsList
import cardDefinitions
from effectDefinitions import effectDefinition
import enemyHelpers
import inventory

# game constants
COSTGAIN = 3
STARTINGDRAW = 5
HANDMAX = 14
PLAYERHEALTHMAX = 50
DIFFICULTYMODIFIER = 0.5
DIFFICULTYSTART = 0.5

# game
playerHealth = 50
costMax = 4
cost = 0
playerBlock = 0
difficulty = DIFFICULTYSTART
turnNumber = 0
roll = []
visibleIntentions = {}
discard = []
hand = []
deck = []
playerEffects = dict({})
playerPermanents = []
enemies = dict({})

# compatability mode
compatability = True

# checkEnemyHealth() -> None
# 
def checkEnemyHealth():
    # https://www.w3schools.com/python/python_variables_global.asp
    global intentionsList
    enemyList = list(enemies.keys())
    for i in range(len(enemyList)):
        # in case the enemies die during it
        try:
            if enemies[enemyList[i]]["health"] <= 0:
                # https://www.w3schools.com/python/ref_list_pop.asp
                enemies.pop(enemyList[i])
                visibleIntentions.pop(enemyList[i])
                i -= 1
        except:
                pass
        # stops overhealing over their max health
        enemyList = list(enemies.keys())
        try:
            if enemies[enemyList[i]]["health"] > intentionsList[enemyList[i]]["health"]:
                enemies[enemyList[i]]["health"] = intentionsList[enemyList[i]]["health"]
        # due to it trying to perform this during your turn, where enemy health is changing too frequently
        except:
            pass

# gainCost(int) -> None
# purpose: takes in an integer called number, then increases cost by number
def gainCost(number):
    global cost
    cost += number

# addPower() -> int
# purpose: if power exists in player effects, return its value. Otherwise return 0
def addPower():
    if "power" in playerEffects:
        return playerEffects["power"]
    else:
        return 0

# addEffect(str,[str],[int],int,bool) -> None
# purpose: takes in two strings, two integers, and a boolean called cardName, name, times, number, and exert.
#           it will then add a dictionary entry to playerEffects called name, with a number equal to number x times.
#           If exert is True, remove a card with the name cardName from the current round.
def addEffect(cardName, name, times, number, exert):
    global playerEffects
    # Loops the amount of times equal to times
    for i in range(times):
        # If name doesn't exist in effects, add it. Otherwise increase it's number.
            if name in playerEffects:
                playerEffects[name] += number
            else:
                playerEffects[name] = number
    # removes the card from the game if exert is True
    if exert:
        discard.remove(cardName)

# checkEffectValid() -> None
# purpose: runs through all effects in playerEffects. If any of them are 0 or below,
#           remove them from the dictionary.
def checkEffectValid():
    global playerEffects
    effectList = list(playerEffects.keys())
    i = 0
    # Checks each effect to see if it is less than zero
    while i < len(effectList):
        if playerEffects[effectList[i]] < 1:
            playerEffects.pop(effectList[i])
        else:
            i += 1

# effectsRun(str,str) -> None
# purpose: takes in two strings called condition and cardName. It will run through all effects in playerEffects,
#           if it finds an effect with a condition that matches condition, it will run it's effect, and reduce
#           it's number by stacksLost (defined in effectDefinition).
def effectsRun(condition, cardName):
    global playerEffects
    global effectDefinition

    # checks each effect to see if it's condition applies
    for effect in playerEffects:
        if effect in effectDefinition and effectDefinition[effect]["condition"] == condition:
            # https://www.w3schools.com/python/ref_func_exec.asp
            currentEffectDef = effectDefinition[effect]
            exec(currentEffectDef["effect"])
            playerEffects[effect] -= currentEffectDef["stacksLost"]
    # add power of suppress is currently on and an ammo card is played
    if "supress" in playerEffects and (cardName in cardDefinitions.ammoList):
        for i in range(playerEffects["supress"]):
            addEffect("", "power", 1, 3, False)
    # checks if the effects are still above 1
    checkEffectValid()

# compSleep(int/float) -> None
# purpose: takes in an integer/float called seconds. If compatability is on,
#           sleeps the program for a number of seconds equal to seconds
def compSleep(seconds):
    global compatability
    if compatability:
        time.sleep(seconds)

# resolveIntentions([str]) -> None
# purpose: takes in a list called resolveList, then executes all strings within the list as functions associated with it's name.
#           Requires the pre-built 'resolveList' variable to work.
# examples:
#           resolveIntentions("damagePlayer(1,2)")                        -> playerHealth - 2
#           resolveIntentions("discardCardRand(2)")                       -> len(hand) - 2
#           resolveIntentions(["damagePlayer(2,2)", "damagePlayer(1,5)"]) -> playerHealth - 7
def resolveIntentions(resolveList):
    global intentionsList
    global roll
    healthList = {}

    # Main loop for each enemies attack
    for attack in resolveList:
        # Health viewing for compatability
        for enemy in enemies:
            healthList[enemy] = enemies[enemy]["health"]

        # printing information for compatability
        helperFuncs.clearTerminal()
        compPrint(healthList)
        compPrint(attack["description"])
        compPrint(f"roll: {roll}")

        #  shows block if it is above 0
        if playerBlock > 0:
            compPrint(playerBlock)

        compPrint(playerHealth)
        compSleep(0.5)
        # executes the function associated with the effect
        exec(attack["effect"])

    # printing updated information
    helperFuncs.clearTerminal()
    compPrint(healthList)
    compPrint(attack["description"])
    compPrint(f"roll: {roll}")
    # if block exists
    if playerBlock > 0:
        compPrint(playerBlock)
    compPrint(playerHealth)

# deckDiscard(int) -> None
# purpose: Takes in an integer called number, then discards cards from your deck equal to number.
def deckDiscard(number):
    global deck
    global discard
    for i in range(number):
        try:
            card = random.randint(0,len(deck) - 1)
            deck.remove(card)
            discard.append(card)
        except:
            # https://www.w3schools.com/python/ref_keyword_pass.asp 
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
        # Loops for a number of times equal to number as long as your hand exists
        while (i < number) and len(hand) > 0:
            # get card is true for is discarding
            discarding = getCard("Card to discard: ", True)
            if discarding in hand:
                # discards the card selected, then gain 1 cost
                discardCard(discarding)
                gainCost(1)
                i += 1
            else:
                # still increase it in case of not wanting to discard in comp mode
                i += 1
                time.sleep(1)
            helperFuncs.clearTerminal()
    except:
        pass

# ammoCard(str,int,int,str) -> None
# purpose: takes in multiple strings and integers called card, times, damage, and effect. It then performs an action based off effect, using
#           times and damage, before replacing itself with the related reload card.
def ammoCard(card,times,damage,effect):
    # determining what happens depending on effect
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
    # https://www.w3schools.com/python/ref_list_remove.asp
    try:
        discard.remove(card)
    except:
        deck.remove(card)
    deck.append(card+"-reload")

# damageEnemyRand(int,int) -> None
# purpose: takes in two integers call times and number, then reduces a random enemies health by
#           number + power a number of times equal to times.
def damageEnemyRand(times,number):
    global enemies
    global roll
    global visibleIntentions
    roll = []
    helperFuncs.clearTerminal()
    # damages a random enemy a number of times equal to times
    for i in range(times):
        enemyList = list(enemies.keys())
        try:
            enemies[enemyList[random.randint(0,len(enemyList)-1)]]["health"] -= (number + addPower())
        except:
            pass
        # add roll for comp mode
        roll.append(number)
        checkEnemyHealth()

# reloadCard(str,int) -> None
# purpose: takes in a string and integer called card and times, and replaces the currently played card
#           with it's loaded counterpart. If times is bigger than one, reload multiple cards in the
#           deck with no regard for names. requires listed card to be in the deck or discard.
def reloadCard(card,times):
    global deck
    global discard
    cardsRemoved = 0
    i = 0
    # checking card played for special purposes
    match card:
        case "blunderbuss":
            damageEnemyAll(1,16)
        case "organ gun":
            gainBlock(1,4)
    # basic effect for normal reloads
    if times == 1:
        deck.append(card)
        try:
            discard.remove(card+"-reload")
        except:
            deck.remove(card+"-reload")
    # secondary effect for tactical reload
    else:
        while (i < len(deck)) and (cardsRemoved <= times):
            card = deck[i]
            if "-reload" in card:
                    # removes the reload from the current card, therefore making it loaded
                    deck.append(card[:-7])
                    deck.remove(card)
                    cardsRemoved += 1
            i += 1
        
# damageEnemyAll(int,int) -> None
# purpose: Takes in two integers called times and numbers, and reduces all enemies
#           hp by times x number + power.
def damageEnemyAll(times,number):
    global enemies
    global roll
    global visibleIntentions
    roll = []
    helperFuncs.clearTerminal()
    # gets enemy list for indexing through it
    enemyList = list(enemies.keys())
    for i in range(len(enemyList)):
        # decrease enemy health a number of times equal to times
        for j in range(times):
            try:
                enemies[enemyList[i]]["health"] -= (number + addPower())
            # in case the enemy dies during this sequence
            except:
                pass
            # updates comp mode values
            roll.append(number)
            visibleIntentions = enemyHelpers.updateEnemyHealth(visibleIntentions,enemies)
            checkEnemyHealth()

# enemyDamageSelf(int,int) -> None
# purpose: takes in two integers called times and number, and reduces the enemies health by number x times.
def enemyDamageSelf(times,number):
    global enemies
    global visibleIntentions
    # modifys enemy health by number a number of times equal to times
    for i in range(times):
        addEnemy = random.choice(list(enemies.keys()))
        enemies[addEnemy]["health"] -= number
        # update visual enemy health for comp
        enemyHelpers.updateEnemyHealth(visibleIntentions,enemies)
        checkEnemyHealth()

# Not used for non-compatability mode
# defineCard() -> None
# purpose: runs a sequence to print the description of cards in compatability mode.
def defineCard():
    print(hand)
    cardInput = input("Which Card: ")
    # try to get card description, else its an invalid card
    try:
        print(cardDefinitions.cardDef[cardInput]["description"])
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
    global roll
    finalNumber = number
    roll = []
    # damage the player loop
    for i in range(times):
        roll.append(number)
        # decrease damage by block if it exists, then decrease block by damage
        if playerBlock > 0:
            finalNumber = number - playerBlock
            playerBlock -= number
        if finalNumber > 0:
            playerHealth -= finalNumber

# getEnemy(str) -> str
# purpose: takes in a string called string. If compatability is active, accept an input,
#           otherwise run getEnemySelected and return either string.
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

# getCard(str, bool) -> str
# purpose: takes in a string and boolean called string and isDiscarding. If compatability
#           mode is active, accept an input, and return it, else run getCardSelected and return
#           it's return
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

# compPrint(str) -> None
# purpose: Takes in a string called string, then prints that string if compatability is active.
def compPrint(string):
    global compatability
    if compatability:
        print(string)

# damageEnemy(int,int) -> None
# purpose: Takes in two integers called times and numbers, then attempts to select an enemy, before
#           reducing it's health by times x number + current power
def damageEnemy(times,number):
    i = 0
    global enemies
    global visibleIntentions
    global roll
    # damages enemy a number of times equal to times
    while i < times:
        helperFuncs.clearTerminal()
        # prints comp mode info
        compPrint(list(enemies.keys()))
        # picks an enemy to target
        target = getEnemy("Choose an enemy: ")
        try:
            enemies[target]["health"] -= (number + addPower())
            i += 1
            # info for comp mode
            roll.append(number)
            enemyHelpers.updateEnemyHealth(visibleIntentions,enemies)
            checkEnemyHealth()
        # in case there are no available enemies, increase iteration    
        except:
            compSleep(0.5)
            i += 1

# gainBlock(int,int) -> None
# purpose: takes in two integers called times and number, and increase playerBlock by the number x times
# examples:
#           gainBlock(1,4) -> playerBlock + 4
#           gainBlock(2,1) -> playerBlock + 2
def gainBlock(times,number):
    global playerBlock
    # loop the number of times to add block
    for i in range(times):
        playerBlock += number

# drawCards(int) -> None
# purpose: takes in an integer called number, and adds cards from the deck to the hand.
# examples:number
#           drawCards(1) -> len(hand) + 1, len(deck) - 1
#           drawCards(2) -> len(hand) + 2, len(deck) - 1
def drawCards(number):
    global discard
    global hand
    global deck
    # loop the times number to draw that many cards
    for i in range(number):
        # if the deck is empty, move the discard pile into the deck
        if len(deck) == 0:
            deck = discard.copy()
            discard.clear()
        # draw a random card from the deck
        selectedCard = deck[random.randint(0, len(deck) - 1)]
        hand.append(selectedCard)
        deck.remove(selectedCard)

# discardCardRand(int) -> None
# purpose: Takes in an integer called number, and randomly discards cards from your hand a number
#           of times equal to number.
# examples:
#           discardCardRand(1) -> len(hand) - 1, len(discard) + 1
#           discardCardRand(4) -> len(hand) - 4, len(discard) + 4
def discardCardRand(number):
    global discard
    global hand
    cardToDiscard = ""
    # main loop to discard random cards
    for i in range(number):
        try:
            cardToDiscard = (hand[random.randint(0,len(hand) - 1)])
            discard.append(cardToDiscard)
            hand.remove(cardToDiscard)
        except:
            pass

# discardCard(str) -> None
# purpose: takes in a string called name, then removes a card in your hand with the same name, and adds it to the discard.
#           Requires the same card to be in hand
# examples:
#           discardCard("strike")      -> len(hand) - 1, len(discard) + 1
#           discardCard("clean sweep") -> len(hand) - 1, len(discard) + 1
def discardCard(name):
    global discard
    global hand
    discard.append(name)
    hand.remove(name)

# resetEffects() -> None
# purpose: clears the players current effects, as well as resets the turn number
def resetEffects():
    global playerEffects
    global turnNumber
    playerEffects.clear()
    turnNumber = 0


# startCombat() -> None
# purpose: initializes a combat encounter by determining enemies, the intentions, and health.
def startCombat():
    global enemies
    global turnNumber
    global deck
    global hand
    global discard
    global playerHealth
    global cost
    global inventory
    global visibleIntentions
    # resets the players resources
    deck = inventory.cards.copy()
    hand = []
    discard = []
    playerHealth = PLAYERHEALTHMAX
    cost = 0
    # sets up the enemies and their intentions
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
    global cardDefinitions
    global turnNumber
    # Give the player their starting resources
    drawCards(STARTINGDRAW)
    cost += COSTGAIN
    playerBlock = 0
    helperFuncs.clearTerminal()
    # Initialization
    compPrint("your turn")
    compSleep(1)
    effectsRun("startTurn", "")
    turnNumber += 1
    # Main game loop
    while True:
        helperFuncs.clearTerminal()
        # end if enemies are dead
        if enemies == {}:
            return
        # sets resources to their max size if they are over it
        while len(hand) > HANDMAX:
            hand.pop()
        if cost > costMax:
            cost = costMax

        # prints information in compatability mode
        compPrint(f"hand: {hand}")
        compPrint(f"discard: {discard}")
        compPrint(f"deck: {deck}")
        compPrint(f"cost: {cost}")
        compPrint(f"health: {playerHealth}")
        compPrint(f"block: {playerBlock}")
        compPrint(visibleIntentions)
        
        # Gets the card you want to play
        playCard = getCard("", False).lower()
        # Attempts to get the designated effect for the selected card
        try:
            effect = cardDefinitions.cardDef[playCard]["effect"]
        except:
                compPrint("Invalid Effect")
                compSleep(1)
        else:
            # Checks if the card is in your hand, and you have sufficent cost to play it
            currentCardCost = cardDefinitions.cardDef[playCard]["cost"]
            if (playCard in hand):
                if cost - currentCardCost > -1:
                    helperFuncs.clearTerminal()
                    # Removes the card from your hand, subtracts cost, and performs the effect designated
                    discardCard(playCard)
                    cost -= currentCardCost
                    effectsRun("cardPlay", playCard)
                    effect = [effect]
                    for run in effect:
                        exec(run)
                    # If the card does not exist (Compatability only)
                else:
                    compPrint("Invalid Card")
                    compSleep(1)
            # performs the defining function if define is inputted (Compatability only)
            elif playCard == "define":
                helperFuncs.clearTerminal()
                exec(effect)
            # Ends your turn
            elif playCard == "end":
                compSleep(1)
                helperFuncs.clearTerminal()
                discardCardRand(len(hand))
                return
            # If the card does not exist (Compatability only)
            else:
                compPrint("Invalid Card")
                compSleep(1)

# enemyTurn() -> None
# purpose: Performs the current intentions listed in the enemies variable, working through all of them and
#           executing the effects
def enemyTurn():
    global playerHealth
    global enemies
    global turnNumber
    global visibleIntentions

    # Performs all the enemies intentions
    for enemy in enemies.keys():
        resolveIntentions(enemies[enemy]["attacks"])
    # Determine next enemies attack
    visibleIntentions = enemyHelpers.determineIntentions(enemies, turnNumber)[1]


# gameLoop(bool) -> bool
# purpose: takes in a boolean called isCompatabilityMode, sets compatability to the boolean, and runs the main loop of the game.
#           If there are no enemies left, returns True, if your health is below 0, return False
# examples:
#           gameLoop(False) -> True
#           gameLoop(True) -> False
def gameLoop(isCompatabilityMode):
    # set compatability
    global compatability
    compatability = isCompatabilityMode

    # set victory and start combat
    won = True
    startCombat()
    # loop until we or all the enemies died
    while enemies != {} and playerHealth > 0:
        playerTurn()
        enemyTurn()
    # if your health is below 0 you lost
    if playerHealth <= 0:
        won = False
        
    return won

# Unable to perform testing due to infinite loop, and outside variables