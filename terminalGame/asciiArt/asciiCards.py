import asciiHelpers

CARD_HEIGHT = 15

asciiCards = {
    "strike" : {
        "small" : {
            "art" : r"""
                   
                   
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
            "len" : 19,
            "height" : CARD_HEIGHT
        },
        
        "large" : {
            "art" : r"""
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
""",
            "len" : 24,
            "height" : CARD_HEIGHT
        }

    }
}


print(asciiHelpers.combineCardStrings(asciiCards["strike"]["small"], asciiCards["strike"]["large"], CARD_HEIGHT))