intentionsList = {
    "goose" : 
        {"turn1" : 
            [
                {"description" : "Deal 2d4 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(2,4))"}, 
                {"description" : "Discard 1 card from your deck", "effect" : "deckDiscard(1)"}
            ], 
        "turn2" : 
            [
                {"description" : "Deal 1d8 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,8))"}, 
                {"description" : "Discard 1 card from your deck", "effect" : "deckDiscard(1)"}
            ],
        "health" : 20,
        "diff" : 1
        },
    "bush" : 
        {"turn2" : 
            [
                {"description" : "Deal 1d4 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,4))"}, 
                {"description" : "Heal an ally for 1d4 health", "effect" : "enemyDamageSelf(1,helperFuncs.diceRoll(1,-4))"}
            ], 
        "turn1" : 
            [
                {"description" : "Deal 1d6 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,6))"}
            ],
        "health" : 12,
        "diff" : 0.5
    },
    "wild bush" : 
        {"turn1" : 
            [
                {"description" : "Deal 1d4 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,4))"}, 
                {"description" : "Heal an ally for 1d4 health", "effect" : "enemyDamageSelf(1,helperFuncs.diceRoll(1,-4))"}
            ], 
        "turn2" : 
            [
                {"description" : "Deal 1d6 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,6))"}
            ],
        "health" : 8,
        "diff" : 0.5
        },
    "tree" : 
        {"turn1" : 
            [
                {"description" : "Deal 2d6 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(2,6))"}, 
                {"description" : "Heal an ally for 1d8 health", "effect" : "enemyDamageSelf(1,helperFuncs.diceRoll(1,-8))"}
            ], 
        "turn2" : 
            [
                {"description" : "Deal 1d12 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,12))"},
                {"description" : "Discard 1 card from your deck", "effect" : "deckDiscard(1)"}
            ],
        "health" : 25,
        "diff" : 1.5
        },
    "canadian goose" : 
        {"turn2" : 
            [
                {"description" : "Deal 7d4 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(7,4))"}, 
            ], 
        "turn1" : 
            [
                {"description" : "Heal an ally for 1d2 health", "effect" : "enemyDamageSelf(1,helperFuncs.diceRoll(1,-2))"},
            ],
        "health" : 45,
        "diff" : 2.5
        },
    "squirrel" : 
        {"turn2" : 
            [
                {"description" : "Heal an ally for 2d6 health", "effect" : "enemyDamageSelf(1,helperFuncs.diceRoll(2,-6))"}
            ], 
        "turn1" : 
            [
                {"description" : "Heal an ally for 1d12 health", "effect" : "enemyDamageSelf(1,helperFuncs.diceRoll(1,-12))"},
            ],
        "health" : 25,
        "diff" : 0.75
        },
    "giant goose" : 
        {"turn1" : 
            [
                {"description" : "Deal 3d12 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(3,12))"}, 
                {"description" : "Discard 5 cards from your deck", "effect" : "deckDiscard(5)"}
            ], 
        "turn2" : 
            [
                {"description" : "Deal 1d36 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,36))"},
                {"description" : "Heal an ally for 2d12 health", "effect" : "enemyDamageSelf(1,helperFuncs.diceRoll(2,-12))"}
            ],
        "health" : 80,
        "diff" : 10
        },
}