# launc mode string
launchMode = r"""
Please full screen your terminal in order for ascii art to display properly,                                                   ‾‾‾‾‾‾|
make sure you can see the frame properly on the top left, this paragraph should only be 3 lines                                ‾‾‾‾| |
If art is not displayed correctly compatibilty mode can be used.                                                                   | |

> Continue[0] - ASCII art, input uses WASD and SPACE
> Compatibility Mode[1] - No ASCII art, input uses characters entered in terminal(for non windows users)

========================================================================================================
[0] Continue    [1] Compatibility Mode
"""

# dictionary of all the art needed for the main menu
mainMenu = {
  "title" : r"""
 ________  ___  ___  _____ ______   ________  _________  ___  ___      ___ _______      
|\   ____\|\  \|\  \|\   _ \  _   \|\   __  \|\___   ___\\  \|\  \    /  /|\  ___ \     
\ \  \___|\ \  \\\  \ \  \\\__\ \  \ \  \|\  \|___ \  \_\ \  \ \  \  /  / | \   __/|    
 \ \_____  \ \  \\\  \ \  \\|__| \  \ \   __  \   \ \  \ \ \  \ \  \/  / / \ \  \_|/__  
  \|____|\  \ \  \\\  \ \  \    \ \  \ \  \ \  \   \ \  \ \ \  \ \    / /   \ \  \_|\ \ 
    ____\_\  \ \_______\ \__\    \ \__\ \__\ \__\   \ \__\ \ \__\ \__/ /     \ \_______\
   |\_________\|_______|\|__|     \|__|\|__|\|__|    \|__|  \|__|\|__|/       \|_______|
   \|_________|                                                                         
""",
  "play" : r"""
                             __  ____  __     __   _  _ 
                             \ \(  _ \(  )   / _\ ( \/ )
                              ) )) __// (_/\/    \ )  / 
                             /_/(__)  \____/\_/\_/(__/  
                 _  _   __   _  _    ____  __     ____  __     __   _  _ 
                / )( \ /  \ / )( \  (_  _)/  \   (  _ \(  )   / _\ ( \/ )
                ) __ ((  O )\ /\ /    )( (  O )   ) __// (_/\/    \ )  / 
                \_)(_/ \__/ (_/\_)   (__) \__/   (__)  \____/\_/\_/(__/ 
                          ___  ____  ____  ____  __  ____  ____ 
                         / __)(  _ \(  __)(    \(  )(_  _)/ ___)
                        ( (__  )   / ) _)  ) D ( )(   )(  \___ \
                         \___)(__\_)(____)(____/(__) (__) (____/
                                   __   _  _  __  ____ 
                                  /  \ / )( \(  )(_  _)
                                 (  O )) \/ ( )(   )(  
                                  \__\)\____/(__) (__)
""",
  "htp" : r"""
                                 ____  __     __   _  _ 
                                (  _ \(  )   / _\ ( \/ )
                                 ) __// (_/\/    \ )  / 
                                (__)  \____/\_/\_/(__/  
            __   _  _   __   _  _    ____  __     ____  __     __   _  _ 
            \ \ / )( \ /  \ / )( \  (_  _)/  \   (  _ \(  )   / _\ ( \/ )
             ) )) __ ((  O )\ /\ /    )( (  O )   ) __// (_/\/    \ )  / 
            /_/ \_)(_/ \__/ (_/\_)   (__) \__/   (__)  \____/\_/\_/(__/  
                          ___  ____  ____  ____  __  ____  ____ 
                         / __)(  _ \(  __)(    \(  )(_  _)/ ___)
                        ( (__  )   / ) _)  ) D ( )(   )(  \___ \
                         \___)(__\_)(____)(____/(__) (__) (____/
                                   __   _  _  __  ____ 
                                  /  \ / )( \(  )(_  _)
                                 (  O )) \/ ( )(   )(  
                                  \__\)\____/(__) (__)
""",
  "credits" : r"""
                                 ____  __     __   _  _ 
                                (  _ \(  )   / _\ ( \/ )
                                 ) __// (_/\/    \ )  / 
                                (__)  \____/\_/\_/(__/  
                 _  _   __   _  _    ____  __     ____  __     __   _  _ 
                / )( \ /  \ / )( \  (_  _)/  \   (  _ \(  )   / _\ ( \/ )
                ) __ ((  O )\ /\ /    )( (  O )   ) __// (_/\/    \ )  / 
                \_)(_/ \__/ (_/\_)   (__) \__/   (__)  \____/\_/\_/(__/  
                    __    ___  ____  ____  ____  __  ____  ____ 
                    \ \  / __)(  _ \(  __)(    \(  )(_  _)/ ___)
                     ) )( (__  )   / ) _)  ) D ( )(   )(  \___ \
                    /_/  \___)(__\_)(____)(____/(__) (__) (____/
                                   __   _  _  __  ____ 
                                  /  \ / )( \(  )(_  _)
                                 (  O )) \/ ( )(   )(  
                                  \__\)\____/(__) (__)
""",
  "quit" : r"""
                                 ____  __     __   _  _ 
                                (  _ \(  )   / _\ ( \/ )
                                 ) __// (_/\/    \ )  / 
                                (__)  \____/\_/\_/(__/  
                 _  _   __   _  _    ____  __     ____  __     __   _  _ 
                / )( \ /  \ / )( \  (_  _)/  \   (  _ \(  )   / _\ ( \/ )
                ) __ ((  O )\ /\ /    )( (  O )   ) __// (_/\/    \ )  / 
                \_)(_/ \__/ (_/\_)   (__) \__/   (__)  \____/\_/\_/(__/  
                          ___  ____  ____  ____  __  ____  ____ 
                         / __)(  _ \(  __)(    \(  )(_  _)/ ___)
                        ( (__  )   / ) _)  ) D ( )(   )(  \___ \
                         \___)(__\_)(____)(____/(__) (__) (____/
                             __    __   _  _  __  ____ 
                             \ \  /  \ / )( \(  )(_  _)
                              ) )(  O )) \/ ( )(   )(  
                             /_/  \__\)\____/(__) (__)
""",
  "controls" : r"""
==========================================================================================
[W] up    [S] down    [Space] select
"""
}

# getMainMenuArt() -> (str, str, str, str)
# purpose: returns ASCII art strings for each main menu option (quit, credits, htp, play)
#          in a tuple for each option last to first
# examples:
#          getMainMenuArt() -> (title+quit+controls, title+credits+controls, title+htp+controls, title+play+controls)
def getMainMenuArt():
  return (str(mainMenu["title"]) + str(mainMenu["quit"]) + str(mainMenu["controls"]), 
          str(mainMenu["title"]) + str(mainMenu["credits"]) + str(mainMenu["controls"]),
          str(mainMenu["title"]) + str(mainMenu["htp"]) + str(mainMenu["controls"]),
          str(mainMenu["title"]) + str(mainMenu["play"]) + str(mainMenu["controls"]),
  )

# dictionary for all the art needed in the play menu
playMenu = {
  "background" : r"""
                                   ___                                                    .
                               ,-""   `.                                                  .
                             ,'  _   e )`-._                                              .
                            /  ,' `-._<.===-'                                             .
                           /  /                                                           .
                          /  ;                         ####################################
              _          /   ;                         ###########              ###########
 (`._    _.-"" ""--..__,'    |                         ####################################
 <_  `-""                     \                        ##     .      .      .      .     ##
  <`-                          :                       #|     |      |      |      |     ##
   (__   <__.                  ;                       #|=====#======#======#======#=====##
     `-.   '-.__.      _.'    /                        #|____###____###____###____###____##
        \      `-.__,-'    _,'                         #|  **    **     **     **     ** |#
         `._    ,    /__,-'                            #|  ##################  ########  |#
            ""._\__,'< <____                           #|  | ##             |  #      |  |#
                 | |  `----.`.                         #|  | #              #  #______|  |#
                 | |        \ `.                       #|  |                #  #======|  |#
                 ; |___      \-``                      #|  |                #  #‾‾‾‾‾‾|  |#
                 \   --<                               #|  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾#  #      |  |#
                  `.`.<                                ####################################
""",
  "playSelected" : r"""
        __  ____  __     __   _  _                             ____  _  _   __  ____               ____   __    ___  __ _ 
        \ \(  _ \(  )   / _\ ( \/ )                           / ___)/ )( \ /  \(  _ \             (  _ \ / _\  / __)(  / )
         ) )) __// (_/\/    \ )  /                            \___ \) __ ((  O )) __/              ) _ (/    \( (__  )  ( 
        /_/(__)  \____/\_/\_/(__/                             (____/\_)(_/ \__/(__)               (____/\_/\_/ \___)(__\_)
""",
  "shopSelected" : r"""
            ____  __     __   _  _                        __   ____  _  _   __  ____               ____   __    ___  __ _ 
           (  _ \(  )   / _\ ( \/ )                       \ \ / ___)/ )( \ /  \(  _ \             (  _ \ / _\  / __)(  / )
            ) __// (_/\/    \ )  /                         ) )\___ \) __ ((  O )) __/              ) _ (/    \( (__  )  ( 
           (__)  \____/\_/\_/(__/                         /_/ (____/\_)(_/ \__/(__)               (____/\_/\_/ \___)(__\_)
""",
  "backSelected" : r"""
            ____  __     __   _  _                             ____  _  _   __  ____           __  ____   __    ___  __ _ 
           (  _ \(  )   / _\ ( \/ )                           / ___)/ )( \ /  \(  _ \          \ \(  _ \ / _\  / __)(  / )
            ) __// (_/\/    \ )  /                            \___ \) __ ((  O )) __/           ) )) _ (/    \( (__  )  ( 
           (__)  \____/\_/\_/(__/                             (____/\_)(_/ \__/(__)            /_/(____/\_/\_/ \___)(__\_)
"""
}

# getCoinMenuControls(int) -> str
# purpose: returns a ASCII string showing controls and the current coin count
#          with the input (coins)
# examples:
#          getCoinMenuControls(10) -> string with "[10] coins"
#          getCoinMenuControls(0) -> string with "[0] coins"
#          getCoinMenuControls(999) -> string with "[999] coins"
def getCoinMenuControls(coins):
  return f"""
===============================================================================================================================
[A] left    [D] right    [Space] select                                                       [{coins}] coins
"""

# getPlayMenuArt(int) -> (str, str, str)
# purpose: returns ASCII art strings for each play menu option (play, shop, back) including coin display
#          witht the parameter coins and returns each optons all in a tuple
# examples:
#          getPlayMenuArt(10) -> (background+playSelected+coins with 10 coins, background+shopSelected+coins with 10 coins, background+backSelected+coins with 10 coins)
#          getPlayMenuArt(0) -> (background+playSelected+coins with 0 coins, background+shopSelected+coins with 0 coins, background+backSelected+coins with 0 coins)
#          getPlayMenuArt(999) -> (background+playSelected+coins with 999 coins, background+shopSelected+coins with 999 coins, background+backSelected+coins with 999 coins)
def getPlayMenuArt(coins):
  return (
    str(playMenu["background"]) + str(playMenu["playSelected"]) + getCoinMenuControls(coins),
    str(playMenu["background"]) + str(playMenu["shopSelected"]) + getCoinMenuControls(coins),
    str(playMenu["background"]) + str(playMenu["backSelected"]) + getCoinMenuControls(coins)
  )

# shop dictionary with all the shop art
shop = {
  "bookshelfHeight" : 12,
  "backSlot" : r"""
__________________
||--------------||
|| [coins] FREE ||
|| ============ ||
|| |   BACK   | ||
|| |  deals   | ||
|| |emotional | ||
|| |damage to | ||
|| |shopkeeper| ||
|| ============ ||
||--------------||
||______________||
""",
  "cards" : {
    "strike" : r"""
______________________________
||--------------------------||
||         [coins] 3        ||
||                          ||
|| ======================== ||
|| |        STRIKE        | ||
|| |   deals 4 damage,    | ||
|| |      1 target        | ||
|| |      cost: 1         | ||
|| ======================== ||
||--------------------------||
||__________________________||
""",
    "crossbow" : r"""
______________________________
||--------------------------||
||         [coins] 6        ||
||                          ||
|| ======================== ||
|| |      CROSSBOW        | ||
|| |   deals 12 damage,   | ||
|| |    requres reload    | ||
|| |      cost: 1         | ||
|| ======================== ||
||--------------------------||
||__________________________||
""",
    "block" : r"""
______________________________
||--------------------------||
||         [coins] 2        ||
||                          ||
|| ======================== ||
|| |        BLOCK         | ||
|| |     gain 3 block     | ||
|| |                      | ||
|| |      cost: 1         | ||
|| ======================== ||
||--------------------------||
||__________________________||
""",
    "clean sweep" : r"""
______________________________
||--------------------------||
||         [coins] 4        ||
||                          ||
|| ======================== ||
|| |     CLEAN SWEEP      | ||
|| |   discard 2 cards,   | ||
|| |  then gain 2 cost    | ||
|| |      cost: 0         | ||
|| ======================== ||
||--------------------------||
||__________________________||
""",
    "well prepared" : r"""
______________________________
||--------------------------||
||         [coins] 4        ||
||                          ||
|| ======================== ||
|| |     WELL PREPARED    | ||
|| |     draw 3 cards     | ||
|| |                      | ||
|| |      cost: 1         | ||
|| ======================== ||
||--------------------------||
||__________________________||
""",
  "blunderbuss" : r"""
______________________________
||--------------------------||
||         [coins] 8        ||
||                          ||
|| ======================== ||
|| |     BLUNDERBUSS      | ||
|| |   deals 2x2 damage   | ||
|| |   requires reload    | ||
|| |      cost: 1         | ||
|| ======================== ||
||--------------------------||
||__________________________||
""",
  "revolver" : r"""
______________________________
||--------------------------||
||         [coins] 6        ||
||                          ||
|| ======================== ||
|| |       REVOLVER       | ||
|| |deals 2d8 damage, 60% | ||
|| |chance to damage again| ||
|| |      cost: 2         | ||
|| ======================== ||
||--------------------------||
||__________________________||
""",
  "cannon" : r"""
______________________________
||--------------------------||
||         [coins] 4        ||
||                          ||
|| ======================== ||
|| |       CANNON         | ||
|| |   deals 4d12 damage  | ||
|| |     to everything    | ||
|| |      cost: 4         | ||
|| ======================== ||
||--------------------------||
||__________________________||
""",
    "multi-strike" : r"""
______________________________
||--------------------------||
||         [coins] 8        ||
||                          ||
|| ======================== ||
|| |     MULTI STRIKE     | ||
|| |   deals 4x3 damage   | ||
|| |    to all enemies    | ||
|| |      cost: 3         | ||
|| ======================== ||
||--------------------------||
||__________________________||
""",
    "organ gun" : r"""
______________________________
||--------------------------||
||         [coins] 6        ||
||                          ||
|| ======================== ||
|| |      ORGAN GUN       | ||
|| |   deals 8d4 damage   | ||
|| |  to random enemies   | ||
|| |      cost: 3         | ||
|| ======================== ||
||--------------------------||
||__________________________||
""",
    "tactical reload" : r"""
______________________________
||--------------------------||
||         [coins] 3        ||
||                          ||
|| ======================== ||
|| |    TACTICAL RELOAD   | ||
|| |    reloads 2 cards   | ||
|| |     in your deck     | ||
|| |      cost: 1         | ||
|| ======================== ||
||--------------------------||
||__________________________||
""",
    "super block" : r"""
______________________________
||--------------------------||
||         [coins] 4        ||
||                          ||
|| ======================== ||
|| |     SUPER BLOCK      | ||
|| |    gain 10 block     | ||
|| |                      | ||
|| |      cost: 2         | ||
|| ======================== ||
||--------------------------||
||__________________________||
""",
  "soldOut" : r"""
______________________________
||--------------------------||
||      [coins] FREE        ||
||                          ||
|| XXXXXXXXXXXXXXXXXXXXXXXX ||
||        SOLD OUT          ||
||   you may be wondering   ||
|| that you didn't buy this ||
|| welp it was 1/14 chance  ||
|| XXXXXXXXXXXXXXXXXXXXXXXX ||
||--------------------------||
||__________________________||
"""
  },
  "select" : {
    "arrow" : r"""
              __             .
             /  \            .
            /    \           .
            ‾‾||‾‾           .
              ||             .
              ‾‾             .
""",
    "blank" : r"""
                             .
                             .
                             .
                             .
                             .
                             .
""",
  "lastArrow" : r"""
        __       .
       /  \      .
      /    \     .
      ‾‾||‾‾     .
        ||       .
        ‾‾
""",
    "height" : 6
  }
}

# all the contrls for the actual game
def getPlayControls(controlName, cost, block, hp):
  playControls = {
    "playCard" : f"""
===============================================================================================================================
Select a card in order to play it, click on the decks in order to view the discard or deck pile, or end your turn
[{hp}] Health  [{block}] Block  [{cost}] Cost                 [A] left    [D] right    [W] up    [S] down    [Space] select  
""",
    "discardCard" : f"""
===============================================================================================================================
Select a card in order to discard it, click on the decks in order to view the discard or deck pile, or end your turn
[{hp}] Health  [{block}] Block  [{cost}] Cost                 [A] left    [D] right    [W] up    [S] down    [Space] select  
  """,
    "selectEnemy" : f"""
===============================================================================================================================
Select an enemy in order to attack it
[{hp}] Health  [{block}] Block  [{cost}] Cost                 [A] left    [D] right    [W] up    [S] down    [Space] select  
"""
  }
  return playControls[controlName]