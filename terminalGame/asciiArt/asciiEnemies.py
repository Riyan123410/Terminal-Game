# constants for art height
ENEMYHEIGHT = 11
ARROWHEIGHT = 6
DESCRIPTIONLEN = 26
DESCRIPTIONHEIGHT = 2

# getArt(str, int) -> str
# purpose: returns ASCII art for a given enemy name from parameter (name)
#          with its health from parameter (hp). If enemy name is wrong returns,
#          "INCORRECT NAME" INFO: make sure HP only has 2 digits otherwise 
#          ASCII art will get messed up and make sure the parameter (currentAttack)
#          is preformated or it will mess up ASCII art
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
         -=(O  "\_     |
           /|  \__\     |
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

# no tests because ASCII art

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

