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

[ENTER] to go back
""")
    input()
    return "mainMenu"