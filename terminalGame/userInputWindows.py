try:
    import msvcrt
except:
    print("not compatable")


# getInput() -> str/byte
# purpose: returns a single key press from the keyboard without
#          requiring the enter key to be pressed
def getInput():
    # get character without pressing enter
    char = msvcrt.getch()
    try:
        # try to convert char from a byte to a string
        char = char.decode('ASCII')
    except:
        # if failed to convert just pass and return the byte directly 
        pass
    return char


# getInputList() -> {}
# purpose: reads a single key press and converts it into a
#          directional input dictionary for movement and actions
#          without needing to press enter
#          "xDir" will return 1 if d is pressed, -1 if a is pressed
#          "yDir" with return 1 if w is pressed, -1 if s is pressed
#          "space" will return true if space is pressed else false
#          if nothing on xDir or yDir is pressed they will return 0
def getInputList():
    # set input to 0 and get the key presses
    inputList = {
        "xDir" : 0,
        "yDir" : 0,
        "space" : False
    }
    key = getInput()
    # match inputs
    match key:
        case "d": 
            inputList["xDir"] = 1
        case "a":
            inputList["xDir"] = -1
        case "w":
            inputList["yDir"] = 1
        case "s":  
            inputList["yDir"] = -1
        case " ": 
            inputList["space"] = True

    return inputList


