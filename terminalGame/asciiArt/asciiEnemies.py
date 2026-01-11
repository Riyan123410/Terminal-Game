# constants for art height
ENEMY_HEIGHT = 10
ARROW_HEIGHT = 6
DESCRIPTION_LEN = 25
DESCRIPTION_HEIGHT = 2

# getArt(str, int) -> str
# purpose: returns ASCII art for a given enemy name from parameter (name)
#          with its health from parameter (hp), make sure HP only has 2
#          digits otherwise ASCII art will get messed up
# examples:
#          getArt("bush", 5) -> "bush art" with hp 5
#          getArt("goose", 10) -> "bush art" with hp 10
#          getArt("fsdi", 20) -> "INCORRECT NAME"
def getArt(name, hp, currentAttack):
    art = {
        "bush" : rf"""
       ______           |
      #o# \#|_#,#       |
     ###\ |/   #o#      |
      #  |()     #      |
        ,'  `           |
        BUSH            |
Health: {hp}              |
Intention:              |
{currentAttack}
""",

        "goose" : rf"""
         __             |
      -=(o '|           |
         '.-.\          |
         /|  \\         |
         _\_):,         |
         GOOSE          |
Health: {hp}              |
Intention:              |
{currentAttack}
""",

        "wild bush" : rf"""
          _____         |
      XoX |X|_X,X       |
     XXX\ |/   XoX      |
      X  |()     X      |
        ,'  `           |
       WILD BUSH        |
Health: {hp}              |
Attacks:                |
{currentAttack}
""",

        "tree" : rf"""
        #o###           |
      #####o###         |
     #o#\#|#/###        |
      ###\|/#o#         |
         )|(            |
        TREE            |
Health: {hp}              |
Attacks:                |
{currentAttack}
"""
    }
    try:
        return art[name]
    except:
        return "INCORRECT NAME"

# dictionary for all arrow art
arrow = {
    "arrow" : r"""
          __            .
         /  \           .
        /    \          .
        ‾‾||‾‾          .
          ||            .
          ‾‾            .
""", "blank" : r"""
                        .
                        .
                        .
                        .
                        .
                        .
"""
}
