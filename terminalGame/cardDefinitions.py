cardDef = {
           "end" : ("passes turn", "print('how are you seeing this')", 0), 
           "define" : ("defines a card; no cost",  "defineCard()", 0), 
           "strike" : ("deals 4 damage, 1 target; 1 cost", "damageEnemy(1,4)", 1), 
           "block" : ("gain 3 block; 1 cost", "gainBlock(1,3)", 1), 
           "clean sweep" : ("discard 2 cards, then gain 2 cost; no cost", "discardGain(2)", 0),
           "crossbow" : ("deals 12 damage, requires reload; 1 cost", "ammoCard('crossbow',1,12,'single')", 1),
           "well prepared" : ("draw 4 cards; 1 cost", "drawCards(3)", 1),
           "crossbow-reload" : ("reloads crossbow; 1 cost", "reloadCard('crossbow')", 1),
           "blunderbuss" : ("deals 2x2 damage, requires reload; 1 cost", "ammoCard('blunderbuss',2,2,'single')", 1),
           "blunderbuss-reload" : ("deals 16 damage, reloads blunderbuss; 2 cost", "reloadCard('blunderbuss')", 2),
           "revolver" : ("deals 1d10 damage, 50% chance to damage again; 2 cost", "ammoCard('revolver',1,helperFuncs.diceRoll(1,10),'recursion')", 2),
           "revolver-reload" : ("reloads revolver; 1 cost", "reloadCard('revolver')", 1),
           "cannon" : ("deals 4d8 damage to everything; 4 cost", "damageEnemyAll(4,helperFuncs.diceRoll(1,8))", 4),
           "shridhar" : ("win", "damageEnemyAll(1, 10000000)", 0)
           }
