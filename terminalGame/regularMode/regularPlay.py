import player

def main():
    player.startCombat()
    while player.enemies != {}:
        player.playerTurn()
        player.enemyTurn()
    return "playMenu"