from enemyIntentions import intentionsList
import random

# determinePly(int) -> str
# purpose: takes in an integer call turnNumber, then returns a string dependent on if it is even or odd. Determines every other turn.
# examples:
#           determinePly(1) -> "turn2"
#           determinePly(2) -> "turn1"
def determinePly(turnNumber):
    if turnNumber % 2 == 0:
        return "turn1"
    else:
        return "turn2"

# testing determinePly
assert determinePly(0) == "turn1"
assert determinePly(1) == "turn2"
assert determinePly(2) == "turn1"

# enemyIntentions(str, int) -> [{str}]
# purpose: takes in two strings called enemyName and turnNumber, and returns the effects and description of the attacks corresponding
#           to the ply from the intentions list. specifically requires a pre-built 'enemies' variable from player.
# examples:
#           enemyIntentions("wild bush", 0) -> [{'description': 'deal 1d4 damage', 'effect': 'damagePlayer(1,helperFuncs.diceRoll(1,4))'}, {'description': 'heal an ally for 1d4 health', 'effect': 'enemyDamageSelf(1,helperFuncs.diceRoll(1,-4))'}]
def enemyIntentions(enemyName, turnNumber):
    global intentionsList
    return intentionsList[enemyName][determinePly(turnNumber)].copy()

# testing enemyIntentions
assert enemyIntentions("wild bush", 0) == [{'description': 'Deal 1d4 damage', 'effect': 'damagePlayer(1,helperFuncs.diceRoll(1,4))'}, {'description': 'Heal an ally for 1d4 health', 'effect': 'enemyDamageSelf(1,helperFuncs.diceRoll(1,-4))'}]
assert enemyIntentions("wild bush", 1) == [{'description': 'Deal 1d6 damage', 'effect': 'damagePlayer(1,helperFuncs.diceRoll(1,6))'}]

#### Used for compatability ####
# updateEnemyHealth({str}, {str}) -> {str}
# purpose: takes in two dictionaries called visibleIntentions and Enemies, then updates visualIntentions with the health variable from Enemies.
#           specifically requires a pre-built 'enemies' variable from player, as well as a pre-built 'visibleIntentions' variable.
# examples:
#           updateEnemyHealth()
def updateEnemyHealth(visibleIntentions, enemies):
    enemyList = list(enemies.keys())
    # Updates the visible intentions
    for i in range(len(enemyList)):
        visibleIntentions[enemyList[i]]["health"] = enemies[enemyList[i]]["health"]
    return visibleIntentions

# determineIntentions({str}, int) -> [{str},{str/int}]
# purpose: Takes in a dictionary and integer called enemies and turnNumber. Changes enemies to reflect the current
#           turns intentions, before returning a list of the updated enemies and the new visual intentions.
#           specifically requires a pre-built 'enemies' variable from player.
def determineIntentions(enemies,turnNumber):
    visibleIntentions = {}
    global intentionsList
    enemyList = list(enemies.keys())
    # iterates through all enemies in enemies
    for enemy in enemyList:
        # changes enemies intentions in enemies
        enemies[enemy]["attacks"] = enemyIntentions(enemy,turnNumber)
        # determines visibleIntentions for comp mode
        visibleIntentions[enemy] = {}
        visibleIntentions[enemy]["attacks"] = []
        # adds descriptions to each attack the enemy wants to perform
        for attack in enemies[enemy]["attacks"]:
            visibleIntentions[enemy]["attacks"].append(attack["description"])
            
    visibleIntentions = updateEnemyHealth(visibleIntentions,enemies)
    return [enemies,visibleIntentions]

# determineEnemies({[{str}]}, int) -> {[{str}]}
# purpose: takes in a dictionary and integer called enemies and difficulty, and updates and returns enemies based on the intentionsList.
#           it will attempt to find a suitable enemy, then initialize it into enemies with the basic setup.
#           requires an empty dictionary 'enemies' variable.
# examples:
#            determineEnemies({[{}]}, 1) -> {goose : []}
def determineEnemies(enemies,difficulty):
    global intentionsList
    combatDifficulty = 0
    attempts = 0
    maxAttempts = 15
    # Finds a suitable enemy to match current difficulty, within the given attempts
    while (combatDifficulty < difficulty) and (attempts <= maxAttempts):
        addEnemy = random.choice(list(intentionsList.keys()))
        # Finds a random enemy in the intentions list within the current combat difficulty
        if intentionsList[addEnemy]["diff"] + combatDifficulty <= difficulty:
            # checks if the enemy is currently in the dictionary to avoid artificial difficulty
            if addEnemy not in enemies:
                # initiates the enemy's base
                enemies[addEnemy] = {}
                enemies[addEnemy]["health"] = (intentionsList[addEnemy]["health"])
                combatDifficulty += intentionsList[addEnemy]["diff"]
                # resets attempts
                attempts = 0
            else:
                attempts += 1
        else:
            attempts += 1

    return enemies

# testing cannot be done due random elements in function