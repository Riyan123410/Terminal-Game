intentionsList = {
    "goose" : 
    {"turn1" : 
        {
            1 : {"description" : "deal 2d4 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(2,4))"}, 
            2 : {"description" : "Discard 1 card from your hand", "effect" : "discardCardRand(1)"}
        }, 
    "turn2" : 
        {
            1 : {"description" : "deal 1d8 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,8))"}, 
            2 : {"description" : "Discard 1 card from your hand", "effect" : "discardCardRand(1)"}
        },
    "health" : 20,
    "diff" : 1
    },
    "bush" : 
    {"turn2" : 
        {
            1 : {"description" : "deal 1d4 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,4))"}, 
            2 : {"description" : "heal an ally for 1d4 health", "effect" : "enemyDamageSelf(1,helperFuncs.diceRoll(1,-4))"}
        }, 
    "turn1" : 
        {
            1 : {"description" : "deal 1d6 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,6))"}
        },
    "health" : 12,
    "diff" : 0.5
    },
    "wild bush" : 
    {"turn1" : 
        {
            1 : {"description" : "deal 1d4 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,4))"}, 
            2 : {"description" : "heal an ally for 1d4 health", "effect" : "enemyDamageSelf(1,helperFuncs.diceRoll(1,-4))"}
        }, 
    "turn2" : 
        {
            1 : {"description" : "deal 1d6 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,6))"}
        },
    "health" : 8,
    "diff" : 0.5
    }
}