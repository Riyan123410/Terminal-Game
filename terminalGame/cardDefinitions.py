cardDef = {
    "end": {
        "description": "passes turn",
        "effect": "print('how are you seeing this')",
        "cost": 0
    },
    "define": {
        "description": "defines a card; no cost",
        "effect": "defineCard()",
        "cost": 0
    },
    "strike": {
        "description": "deals 4 damage, 1 target; 1 cost",
        "effect":"damageEnemy(1, 4)",
        "cost": 1
    },
    "block": {
        "description": "gain 3 block; 1 cost",
        "effect": "gainBlock(1, 3)",
        "cost": 1
    },
    "clean sweep": {
        "description": "discard 2 cards, then gain 2 cost; no cost",
        "effect": "discardGain(2)",
        "cost": 0
    },
    "crossbow": {
        "description": "deals 12 damage, requires reload; 1 cost",
        "effect": "ammoCard('crossbow', 1, 12, 'single')",
        "cost": 1
    },
    "well prepared": {
        "description": "draw 3 cards; 1 cost",
        "effect": "drawCards(3)",
        "cost": 1
    },
    "crossbow-reload": {
        "description": "reloads crossbow; 1 cost",
        "effect": "reloadCard('crossbow', 1)",
        "cost": 1
    },
    "blunderbuss": {
        "description": "deals 2x2 damage, requires reload; 1 cost",
        "effect": "ammoCard('blunderbuss', 2, 2, 'single')",
        "cost": 1
    },
    "blunderbuss-reload": {
        "description": "deals 16 damage, reloads blunderbuss; 2 cost",
        "effect": "reloadCard('blunderbuss', 1)",
        "cost": 2
    },
    "revolver": {
        "description": "deals 2d8 damage, 60% chance to damage again; 2 cost",
        "effect": "ammoCard('revolver', 1, helperFuncs.diceRoll(2, 8), 'recursion')",
        "cost": 2
    },
    "revolver-reload": {
        "description": "reloads revolver; 1 cost",
        "effect": "reloadCard('revolver', 1)",
        "cost": 1
    },
    "cannon": {
        "description": "deals 4d12 damage to everything; 4 cost",
        "effect": "damageEnemyAll(4, helperFuncs.diceRoll(1, 12))",
        "cost": 4
    },
    "shridhar": {
        "description": "win",
        "effect": "damageEnemyAll(1, 10000000)",
        "cost": 0
    },
    "multi-strike": {
        "description": "deals 4x3 damage to all enemies; 3 cost",
        "effect": "damageEnemyAll(3, 4)",
        "cost": 3
    },
    "organ gun": {
        "description": "deals 8d4 damage to random enemies; 2 cost",
        "effect": "ammoCard('organ gun', 4, 8, 'all')",
        "cost": 2
    },
    "organ gun-reload": {
        "description": "gain 4 block, reloads organ gun; 2 cost",
        "effect": "reloadCard('organ gun', 1)",
        "cost": 2
    },
    "tactical reload": {
        "description": "reloads 2 cards in your deck; 1 cost",
        "effect": "reloadCard('all', 2)",
        "cost": 1
    },
    "super block": {
        "description": "gain 10 block; 2 cost",
        "effect": "gainBlock(1, 10)",
        "cost": 2
    }
}
    
