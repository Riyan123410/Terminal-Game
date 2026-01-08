import sys

def getInput():
    try:
        # for windows
        import msvcrt
        # get character without pressing enter
        char = msvcrt.getch()
        # ignore special keys which come as a prefix + code
        if char in (b'\x00', b'\xe0'):
            # call getch again for the second part of the special key, than return blank
            msvcrt.getch()
            return ''
        try:
            # try to convert char from a byte to a string
            char = char.decode('ASCII')
        except:
            # if failed to convert just pass and return the byte directly 
            pass
        return char
    except ImportError:
        # for linux/macOS
        import tty, termios

        # Get the file descriptor for standard input (keyboard)
        fileDescriptor = sys.stdin.fileno()  
        # Save the current terminal settings it can be restored later
        originalTerminalSettings = termios.tcgetattr(fileDescriptor)

        try:
            # Set the terminal to raw mode so you dont need to press enter
            tty.setraw(fileDescriptor)
            # Read a single character
            char = sys.stdin.read(1)  
        finally:
            # Restore the original terminal settings to fix it
            termios.tcsetattr(fileDescriptor, termios.TCSADRAIN, originalTerminalSettings)

        # Return the single character pressed
        return char

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

