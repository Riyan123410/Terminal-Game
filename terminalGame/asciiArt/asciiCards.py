CARD_HEIGHT = 11
CARD_DOWN_HEIGHT = 2

# dictionary for all card art
art = {
    "strike" : {
        "normal" : r"""
                   
                   
 _.-._.-._.-._.-._ 
(                 )
 )       .    1  ( 
(       / \       )
 )      |.|      ( 
(       |:|       )
 )     --8--     ( 
(        8        )
 `-._.-._.-._.-.-' 
""",
        "selected" : r"""
 _.-._.-._.-._.-._.-._. 
(                      )
 )  .              1  ( 
(  / \     STRIKE      )
 ) | |                ( 
(  |.|                 )
 ) |.| deals 4 damage ( 
(  |:|    1 target     )
 )--8--               ( 
(   8                  )
 `-._.-._.--._.-._.-.-' 
"""
    },
    "block" : {
        "normal" : r"""
                   
                   
 _.-._.-._.-._.-._ 
(                 )
 )             1  ( 
(                 )
 )   |`-_/\_-`|  ( 
(    |   ||   |   )
 )    \  ||  /   ( 
(      \____/     )
 `-._.-._.-._.-.-' 
""",
        "selected" : r"""
 _.-._.-._.-._.-._.-._. 
(                      )
 )                1   ( 
(                      )
 )|`-_/\_-`|   BLOCK  ( 
( |   ||   |           )
 ) \  ||  /    Gain   ( 
(   \____/    3 block  )
 )                    ( 
(                      )
 `-._.-._.--._.-._.-.-' 
"""
    },
    "clean sweep" : {
        "normal" : r"""
                   
                   
 _.-._.-._.-._.-._
(                 )
 )       |       (
(        |        )
 )       |       (
(        |        )
 )      /X\      (
(      //X\\      )
 `-._.-._.-._.-.-'
""",
        "selected" : r"""
 _.-._.-._.-._.-._.-._. 
(                      )
 )   |            1   ( 
(    |                 )
 )   |   CLEAN SWEEP  ( 
(    |                 )
 )   |    discard 2   ( 
(   /X\   cards then   )
 ) //X\\  gain 2 cost ( 
(                      )
 `-._.-._.--._.-._.-.-' 
"""
    },
    "crossbow" : {
        "normal" : r"""
                   
                   
 _.-._.-._.-._.-._ 
(      .-.        ) 
 )     /  \\     ( 
( .---/-+--||     ) 
 )|  K=====++->  ( 
( '---\-+--||     ) 
 )      \  //    ( 
(       `-'       )
 `-._.-._.-._.-.-' 
""",
        "selected" : r"""
 _.-._.-._.-._.-._.-._. 
(                      )
 )   |            1   ( 
(    |                 )
 )   |   CLEAN SWEEP  ( 
(    |                 )
 )   |    discard 2   ( 
(   /X\   cards then   )
 ) //X\\  gain 2 cost ( 
(                      )
 `-._.-._.--._.-._.-.-' 
"""
    },
    "decks" : {
        "deckSelected" : r"""
 ____________________                   ____________________
| \                   \                | \                   \
|  \___________________\               |  \___________________\
 \ |     <<DECK>>       |               \ |    DISCARD PILE    |
  \|____________________|                \|____________________|
""",
        "discardSelected" : r"""
 ____________________                   ____________________
| \                   \                | \                   \
|  \___________________\               |  \___________________\
 \ |       DECK         |               \ |  <<DISCARD PILE>>  |
  \|____________________|                \|____________________|
""",
        "nonSelected" : r"""
 ____________________                   ____________________
| \                   \                | \                   \
|  \___________________\               |  \___________________\
 \ |       DECK         |               \ |    DISCARD PILE    |
  \|____________________|                \|____________________|
"""
    }
}

# getDeckArt() -> (str, str, str)
# purpose: returns ASCII art strings in a tuple for deck states: 
#          selected, discard selected, and non-selected
# examples:
#          getDeckArt() -> ("deckSelected art", "discardSelected art", "nonSelected art)"
def getDeckArt():
    return(
        str(art["decks"]["deckSelected"]),
        str(art["decks"]["discardSelected"]),
        str(art["decks"]["nonSelected"])
    )