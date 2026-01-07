from enemyIntentions import intentionsList
import random


def enemyIntentions(enemyName, turnNumber):
    global intentionsList
    attackIntentions = []
    for i in range(len(intentionsList[enemyName][determinePly(turnNumber)])):
        attackIntentions.append(intentionsList[enemyName][determinePly(turnNumber)][i+1])
    return attackIntentions
    
def determinePly(turnNumber):
    if turnNumber % 2 == 0:
        return "turn1"
    else:
        return "turn2"
    
def determineIntentions(enemies,turnNumber):
    visibleIntentions = {}
    global intentionsList
    enemyList = list(enemies.keys())
    print(enemyList)
    for i in range(len(enemyList)):
        print(enemies)
        enemies[enemyList[i]]["attacks"] = enemyIntentions(enemyList[i],turnNumber)
        print(enemies)
        visibleIntentions[enemyList[i]] = {}
        for e in range(len(intentionsList[enemyList[i]][determinePly(turnNumber)])):
            visibleIntentions[enemyList[i]][e] = (enemies[enemyList[i]]["attacks"][e]["description"])
    return [enemies,visibleIntentions]

def determineEnemies(enemies,difficulty):
    combatDifficulty = 0
    global intentionsList
    while combatDifficulty < difficulty:
        addEnemy = random.choice(list(intentionsList.keys()))
        if intentionsList[addEnemy]["diff"] + combatDifficulty <= difficulty:
            if addEnemy not in enemies:
                enemies[addEnemy] = {}
                enemies[addEnemy]["health"] = (intentionsList[addEnemy]["health"])
                combatDifficulty += intentionsList[addEnemy]["diff"]
    return enemies