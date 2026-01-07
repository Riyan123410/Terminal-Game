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
    {"turn1" : 
        {
            1 : {"description" : "deal 1d4 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,4))"}, 
            2 : {"description" : "gain 1d4 health", "effect" : "discardCardRand(1)"}
        }, 
    "turn2" : 
        {
            1 : {"description" : "deal 1d8 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,8))"}, 
            2 : {"description" : "Discard 1 card from your hand", "effect" : "discardCardRand(1)"}
        },
    "health" : 20,
    "diff" : 1
    }
}