import os
import random


# clamp(int/float, int/float, int/float) -> int/float
# purpose: sets the paramater (maxNum) to be at least the entered input (minNum)
#          and at most the parameter (maxNum)
# examples:
#          clamp(5, 0, 10) -> 5
#          clamp(-5.6, -2.1, 10) -> -2.1
#          clamp(0, 0, 0) -> 0
def clamp(num, minNum, maxNum):
    # if num is less than min num return the min
    if num < minNum:
        return minNum
    # if its greater return max
    if num > maxNum:
        return maxNum
    # otherwise return the number
    return num

# tests for clamp
assert clamp(5, 10, 20) == 10
assert clamp(25, 10, 20) == 20
assert clamp(10, 10, 20) == 10
assert clamp(20, 10, 20) == 20
assert clamp(15, 10, 20) == 15
assert clamp(-5, -10, 0) == -5
assert clamp(-15, -10, 0) == -10
assert clamp(5, -10, 0) == 0

# changeWithClamp(int/float, int/float, int/float, int/float) -> int/float
# purpose: takes in the number (num) adding the parameter (change) it than
#          clamps this number to be withen (minNum) and (maxNum)
# examples:
#          changeWithClamp(5, 3, 0, 10) -> 8
#          changeWithClamp(5, -10, 0, 10) -> 0
#          changeWithClamp(5.5, 10, 0, 10.5) -> 10.5
def changeWithClamp(num, change, minNum, maxNum):
    return clamp(num + change, minNum, maxNum)

# tests for changeWithClamp
assert changeWithClamp(10, 5, 0, 20) == 15
assert changeWithClamp(10, -5, 0, 20) == 5
assert changeWithClamp(18, 5, 0, 20) == 20
assert changeWithClamp(2, -5, 0, 20) == 0
assert changeWithClamp(15, 5, 0, 20) == 20
assert changeWithClamp(5, -5, 0, 20) == 0
assert changeWithClamp(10, 0, 0, 20) == 10
assert changeWithClamp(-5, -10, -20, -1) == -15
assert changeWithClamp(-5, -20, -20, -1) == -20
assert changeWithClamp(-15, 10, -20, -1) == -5

# clearTerminal() -> None
# purpose: Clears the terminal based on the current operating system
def clearTerminal():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        os.system('cls')
    else:
        # Command for Linux and macOS
        os.system('clear')


# diceRoll(int, int) -> int
# purpose: returns the sum of a random number from 1 to the input (size)
#          the number of numbers generated are based on the parameter (times)
def diceRoll(times,size):
    # reset roll
    roll = 0
    # only run if size is greater than 0
    if size > 0:
        # loop through adding each dice roll
        for i in range(times):
            roll += random.randint(1,size)
    else:
        # negative number for healing
        for i in range(times):
            roll += random.randint(size,-1)
    return roll


# removeEndlinesInList([str]) -> [str]
# purpose: removes newline characters from each string in a list and filters out empty strings
# examples:
#          removeEndlinesInList(["a\n", "\n", "b\n"]) -> ["a", "b"]
#          removeEndlinesInList(["\n", "\n"]) -> []
#          removeEndlinesInList(["how are\nyou", "test\n"]) -> ["how areyou", "test"]
def removeEndlinesInList(stringList):
    # make sure it doesnt change original variable
    newList = []
    for string in stringList:
        # do an if statment to check if we arent just appending an empty string
        replacedEndlines = string.replace("\n", "")
        if replacedEndlines != "":
            newList.append(replacedEndlines)
    return newList

# tests for removeEndLinesInList
assert removeEndlinesInList(["hello\n", "world\n"]) == ["hello", "world"]
assert removeEndlinesInList(["\n", "\n\n"]) == []
assert removeEndlinesInList(["a\nb\nc", "d\ne\nf"]) == ["abc", "def"]
assert removeEndlinesInList(["no newlines", "still clean"]) == ["no newlines", "still clean"]
assert removeEndlinesInList(["\nstart", "end\n", "\nmiddle\n"]) == ["start", "end", "middle"]
assert removeEndlinesInList([]) == []