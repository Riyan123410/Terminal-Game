# main() -> "mainMenu"
# purpose: this is the main function for the game credits, prints the credits and waits
#          until the user enters anything in the console to which it would always return 
#          "mainMenu" for the next game state
# examples:
#          main() -> "mainMenu"
def main():
    print(r"""
CREDITS:
Alex and Riyan

ASCII ART:
https://ascii.co.uk/art/goose -> first goose
https://www.asciiart.eu/art-and-design/borders -> wavy by unkown
https://patorjk.com/software/taag/ -> used for all ascii text

[ENTER] to go back
""")
    input()
    return "mainMenu"