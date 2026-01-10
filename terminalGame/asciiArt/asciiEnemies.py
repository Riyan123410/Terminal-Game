ENEMY_HEIGHT = 11
ARROW_HEIGHT = 6

def getArt(name, hp):
    art = {
        "bush" : rf"""
BUSH   ______           |
      #o# \#|_#,#       |
     ###\ |/   #o#      |
      #  |()     #      |
        ,'  `           |
Health: {hp}              |
Attacks:                |
    1) deal 1d4 damage  |
    2) heal an ally for |
       1d4 health       |
    3) deal 1d6 damage  |
""",

        "goose" : rf"""
GOOSE    __             |
      -=(o '|           |
         '.-.\          |
         /|  \\         |
         _\_):,         |
Health: {hp}              |
Attacks:                |
    1) deal 2d4 damage  |
    2) Discard 1 card   |
       from your deck   |
    3) deal 1d8 damage  |
""",

        "wild bush" : rf"""
WILD BUSH _____         |
      XoX |X|_X,X       |
     XXX\ |/   XoX      |
      X  |()     X      |
        ,'  `           |
Health: {hp}              |
Attacks:                |
    1) deal 1d4 damage  |
    2) heal an ally for |
       1d4 health       |
    3) deal 1d6 damage  |
""",

        "tree" : rf"""
TREE   ###o##           |
      #\#|#/##          |
        )|(             |
Health: {hp}              |
Attacks:                |
    1) deal 2d6 damage  |
    2) heal an ally for |
       1d8 health       |
    3) deal 1d12 damage |
    4) discard 1 card   |
       from your deck   |
"""
    }
    return art[name]

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
