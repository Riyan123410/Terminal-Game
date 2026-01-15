import os
import random
import math


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
    # https://www.w3resource.com/python-exercises/python-basic-exercise-99.php 
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

# no tests because random


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
assert removeEndlinesInList(["no newlines", "billy bob"]) == ["no newlines", "billy bob"]
assert removeEndlinesInList(["\nstart", "end\n", "\nmiddle\n"]) == ["start", "end", "middle"]
assert removeEndlinesInList(["", ""]) == []
assert removeEndlinesInList([]) == []

# shoppingItems() -> None
# purpose: prints the sqrt of the length of the word apple, then prints
#          the current shopping lists, asks the user a question, finally
#          creates shopping.txt (if it doesnt exist) and re writes it.
#          This is just an extra function used for examples
def shoppingItems():    

    # create a list of lists
    shoppingLists = [
        ["bread", "mayo", "cheese", "fish", "cheese", "mayo", "bread"],
        ["bowl", "stock", "fish", "carrot", "corn", "spinach", "water"],
        ["flour", "water", "yeast", "wait", "knead", "bake", "eat"]
    ]

    # loop through shopping lists with lockstep and print it
    for i in range(len(shoppingLists[0])):
        print(shoppingLists[0][i], shoppingLists[1][i], shoppingLists[2][i])

    number = input("how many fish do you know?: ")
    # try to see if the number is an input and print based on that
    try:
        number = int(number)
    except ValueError as e:
        print(f"Mr.Marco would be disappointed in you, because: {e}")
    else:
        if number > 5:
            print(f"Wow! thats a lot! that's like, double than {number / 2}!!")
        else:
            print(f"Fun Fact! if you square root the number its {math.sqrt(number)}?")
    finally:    
        print("Thats so cool! :>")

    # append a file called shopping just in case it doesnt exist
    appendFile = open("shopping.txt", "a")
    # write user input and close
    appendFile.write(f"{number}")
    appendFile.close()

    # read the file and print its contents
    readFile = open("shopping.txt", "r")
    print(readFile.read())
    readFile.close()

    # read the file and write to it
    readPlus = open("shopping.txt", "r+")
    print(readPlus.read())
    # write user input in file and close it
    readPlus.write(f"{number} saved!")
    readPlus.close()

    # read and write file, reseting data when opened
    writePlus = open("shopping.txt", "w+")
    writePlus.write("this file has been reset")
    # reset seek to read file, than close it
    writePlus.seek(0)
    print(writePlus.read())
    writePlus.close()

    # open file in append + to also read it
    appendPlus = open("shopping.txt", "a+")
    appendPlus.write("\nappending to file")
    # reset seek to read it and than close file
    appendPlus.seek(0)
    print(appendPlus.read())
    appendPlus.close()