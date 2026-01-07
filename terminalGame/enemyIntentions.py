intentionsList = {"goose" : 
                  {"turn1" : {"attackTimes" : 2, 
                              1 : {"description" : "deal 2d4 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(2,4))"}, 
                              2 : {"description" : "Discard 1 card from your hand", "effect" : "discardCardRand(1)"}
                              }, 
                    "turn2" : {"attackTimes" : 2, 
                                1 : {"description" : "deal 1d8 damage", "effect" : "damagePlayer(1,helperFuncs.diceRoll(1,8))"}, 
                                2 : {"description" : "Discard 1 card from your hand", "effect" : "discardCardRand(1)"}
                                }
                    }
                 }