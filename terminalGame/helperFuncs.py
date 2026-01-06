import os

def clamp(num, minNum, maxNum):
    if num < minNum:
        return minNum
    if num > maxNum:
        return maxNum
    return num

# change and clamp
def changeWithClamp(num, change, minNum, maxNum):
    return clamp(num + change, minNum, maxNum)

# clear the terminal
def clearTerminal():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        os.system('cls')
    else:
        # Command for Linux and macOS
        os.system('clear')