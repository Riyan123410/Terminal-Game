import asciiHelpers

CARD_HEIGHT = 15
CARD_DOWN_HEIGHT = 2

asciiCards = {
    "strike" : {
        "normal" : r"""
                   
                   
 _.-._.-._.-._.-._ 
(                 )
 )       .       ( 
(       / \       )
 )      | |      ( 
(       | |       )
 )      |.|      ( 
(       |.|       )
 )      |:|      ( 
(       |:|       )
 )     --8--     ( 
(        8        )
 `-._.-._.-._.-.-' 
""",
        "selected" : r"""
 _.-._.-._.-._.-._.-._. 
(                      )
 )          .         ( 
(          / \         )
 )         | |        ( 
(          |.|         )
 )         |.|        ( 
(          |:|         )
 )        --8--       ( 
(           8          )
 )                    ( 
(         STRIKE       )
 )   deals 4 damage,  ( 
(        1 target      )
 `-._.-._.--._.-._.-.-' 
"""
    },
    "cardDown" : r"""
 _.-._.-._.-._.-._.-._. 
(                      )
"""
}
# print(asciiHelpers.combineCardStrings([asciiCards["strike"]["selected"], asciiCards["strike"]["normal"]], CARD_HEIGHT))