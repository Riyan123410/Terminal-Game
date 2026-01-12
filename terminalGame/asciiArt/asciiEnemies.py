# constants for art height
ENEMY_HEIGHT = 11
ARROW_HEIGHT = 6
DESCRIPTION_LEN = 26
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
BUSH   ______           |
      #o# \#|_#,#       |
     ###\ |/   #o#      |
        ,'  `           |
Health: {hp}              |
Intention:              |
{currentAttack}
""",
        "goose" : rf"""
GOOSE     __            |
      -=(o '|           |
         /|  \          |
         _\_):,         |
Health: {hp}              |
Intention:              |
{currentAttack}
""",

        "wild bush" : rf"""
WILD BUSH _____         |
      XoX |X|_X,X       |
     XXX\ |/   XoX      |
        ,'  `           |
Health: {hp}              |
Intention:              |
{currentAttack}
""",
        "tree" : rf"""
TREE  #####o###         |
     #o#\#|#/###        |
      ###\|/#o#         |
         )|(            |
Health: {hp}              |
Intention:              |
{currentAttack}
""",
        "canadian goose" : rf"""
CANADIAN GOOSE  __      |
   o____     -=(o '|    |
   ||X||       /|  \    |
   |           _\_):,   |
Health: {hp}              |
Intention:              |
{currentAttack}
""",
        "squirrel" : rf"""
SQUIRREL __   />>       |
        (_ \.'  ')      |
          \(  )<<       |
           ''---'       |
Health: {hp}              |
Intention:              |
{currentAttack}
""",
        "giant goose" : rf"""
GIANT GOOSE ___        |
         -=(o  "\       |
           /|    \      |
            _\____):,   |
Health: {hp}              |
Intention:              |
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

