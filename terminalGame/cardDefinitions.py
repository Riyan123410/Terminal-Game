cardDef = {
           "end" : ["passes turn", "print('how are you seeing this')", 0], 
           "define" : ["defines a card; no cost",  "defineCard()", 0], 
           "strike" : ["deals 4 damage, 1 target; 1 cost", "damageEnemy(1,4)", 1], 
           "block" : ["gain 3 block; 1 cost", "gainBlock(1,3)", 1], 
           "clean sweep" : ["discard 2 cards, then gain 2 cost; no cost", "discardGain(2)", 0],
           "crossbow" : ["deals 12 damage, requires reload; 1 cost", "ammoCard('crossbow',1,12,'single')", 1],
           "well prepared" : ["draw 4 cards; 1 cost", "drawCards(3)", 1],
           "crossbow-reload" : ["reloads crossbow; 1 cost", "reloadCard('crossbow')", 1],
           "blunderbuss" : ["deals 2x2 damage, requires reload; 1 cost", "ammoCard('blunderbuss',2,2,'single')", 1],
           "blunderbuss-reload" : ["deals 16 damage, reloads blunderbuss; 2 cost", "reloadCard('blunderbuss')", 2]
           }
