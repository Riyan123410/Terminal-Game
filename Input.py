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
            char = char.decode('latin1')
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
    inputList = [0,0,0]
    key = getInput()
    # horizontal
    match key:
        case "d": 
            inputList[0] = 1
        case "a":
            inputList[0] = -1
        case "w":
            inputList[1] = 1
        case "s":  
            inputList[1] = -1
        case " ": 
            inputList[2] = 1

    return inputList

