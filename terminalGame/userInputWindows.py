try:
    import msvcrt
except:
    print("not compatable")

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

    
def getInputList():
    # set input to 0 and get the key presses
    inputList = [0,0,0]
    key = getInput()
    # horizontal
    if key == "d":
        inputList[0] = 1
    if key == "a":
        inputList[0] = -1
    # vertical
    if key == "w":
        inputList[1] = 1
    if key == "s":
        inputList[1] = -1

    # other key
    inputList[2] = key
    
    return inputList

