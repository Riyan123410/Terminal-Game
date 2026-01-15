try:
    # https://www.w3schools.com/python/ref_module_msvcrt.asp
    import msvcrt
except:
    print("not compatable")


# getInput() -> str/byte
# purpose: returns a single key press from the keyboard without
#          requiring the enter key to be pressed
def getInput():
    # get character without pressing enter
    # char = msvcrt.getch()
    # try:
    #     # try to convert char from a byte to a string
    #     # https://stackoverflow.com/questions/15599565/how-do-you-use-msvcrt-getch-to-extract-and-use-input 
    #     char = char.decode('ASCII')
    # except:
    #     # if failed to convert just pass and return the byte directly 
    #     pass
    return msvcrt.getwch()


# getInputDict() -> {}
# purpose: reads a single key press and converts it into a
#          directional input dictionary for movement and actions
#          without needing to press enter
#          "xDir" will return 1 if d is pressed, -1 if a is pressed
#          "yDir" with return 1 if w is pressed, -1 if s is pressed
#          "space" will return true if space is pressed else false
#          if nothing on xDir or yDir is pressed they will return 0
def getInputDict():
    # set input to 0 and get the key presses
    inputDict = {
        "xDir" : 0,
        "yDir" : 0,
        "space" : False
    }
    key = getInput()
    # map inputs to -1 to 1 and space to true/false
    match key:
        case "d": 
            inputDict["xDir"] = 1
        case "a":
            inputDict["xDir"] = -1
        case "w":
            inputDict["yDir"] = 1
        case "s":  
            inputDict["yDir"] = -1
        case " ": 
            inputDict["space"] = True

    return inputDict


