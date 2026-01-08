from enemyIntentions import intentionsList
import random

# determinePly(int) -> str
# purpose: takes in an integer call turnNumber, then returns a string dependent on if it is even or odd.
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
# to the ply from the intentions list
# examples:
#           enemyIntentions("wild bush", 1) -> [{'description': 'deal 1d4 damage', 'effect': 'damagePlayer(1,helperFuncs.diceRoll(1,4))'}, {'description': 'heal an ally for 1d4 health', 'effect': 'enemyDamageSelf(1,helperFuncs.diceRoll(1,-4))'}]
def enemyIntentions(enemyName, turnNumber):
    global intentionsList
    attackIntentions = []
    for i in range(len(intentionsList[enemyName][determinePly(turnNumber)])):
        attackIntentions.append(intentionsList[enemyName][determinePly(turnNumber)][i+1])
    return attackIntentions

# testing enemyIntentions
assert enemyIntentions("wild bush", 1) == [{'description': 'deal 1d6 damage', 'effect': 'damagePlayer(1,helperFuncs.diceRoll(1,6))'}]
assert enemyIntentions("wild bush", 0) == [{'description': 'deal 1d4 damage', 'effect': 'damagePlayer(1,helperFuncs.diceRoll(1,4))'}, {'description': 'heal an ally for 1d4 health', 'effect': 'enemyDamageSelf(1,helperFuncs.diceRoll(1,-4))'}]

# updateEnemyHealth({str}, {str}) -> {str}
# purpose: takes in two dictionaries called visinleIntentions and Enemies,then updates visualIntentions with the health variable from Enemies.
# examples:
#           updateEnemyHealth()
def updateEnemyHealth(visibleIntentions, enemies):
    enemyList = list(enemies.keys())
    for i in range(len(enemyList)):
        visibleIntentions[enemyList[i]]["health"] = enemies[enemyList[i]]["health"]
    return visibleIntentions

def determineIntentions(enemies,turnNumber):
    visibleIntentions = 0
    visibleIntentions = {}
    global intentionsList
    enemyList = list(enemies.keys())
    for i in range(len(enemyList)):
        enemies[enemyList[i]]["attacks"] = enemyIntentions(enemyList[i],turnNumber)
        visibleIntentions[enemyList[i]] = {}
        visibleIntentions[enemyList[i]]["attacks"] = {}
        for e in range(len(intentionsList[enemyList[i]][determinePly(turnNumber)])):
            visibleIntentions[enemyList[i]]["attacks"][e+1] = (enemies[enemyList[i]]["attacks"][e]["description"])
            visibleIntentions = updateEnemyHealth(visibleIntentions,enemies)
    return [enemies,visibleIntentions]

# determineEnemies({[{str}]}, int) -> {[{str}]}
# purpose: takes in a dictionary(?) and integer called enemies and difficulty, and updates and returns enemies based on the intentionsList.
# examples:
#            determineEnemies({[{}]}, 1) -> {goose : []}
def determineEnemies(enemies,difficulty):
    combatDifficulty = 0
    attempts = 0
    maxAttempts = 15
    global intentionsList
    while (combatDifficulty < difficulty) and (attempts <= maxAttempts):
        addEnemy = random.choice(list(intentionsList.keys()))
        if intentionsList[addEnemy]["diff"] + combatDifficulty <= difficulty:
            if addEnemy not in enemies:
                enemies[addEnemy] = {}
                enemies[addEnemy]["health"] = (intentionsList[addEnemy]["health"])
                combatDifficulty += intentionsList[addEnemy]["diff"]
                attempts = 0
            else:
                attempts += 1
        else:
            attempts += 1

    return enemies