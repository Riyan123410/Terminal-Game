def findWidth(string):
    # replace endlines so you can find it not starting at the begining since that is an endline
    replaceEndlines = string.replace("\n", "~")
    # has to be a symbol not being used from ascii art
    width = replaceEndlines.find("~", 1) - 1
    if width < 0:
        width = 0
    return width

def combineStrings(string1, string2, width1, height):
    # find width of strings
    width2 = findWidth(string2)
    # remove all end lines and create a new string
    string1 = string1.replace("\n", "")
    string2 = string2.replace("\n", "")
    combinedString = ""
    # loop through the height of the strings
    for i in range(height):
       # loop through the legnth of each adding to the new string
        try:
            combinedString += string1[i * width1 : i * width1 + width1]
            combinedString += string2[i * width2 : i * width2 + width2]
        except IndexError:
            return "OUT OF RANGE"
        combinedString += "\n"
    return combinedString

def combineCardStrings(stringDicts, height):
    # set string and len
    combinedString = ""
    width = 0
    # loop through each card and add them
    for card in stringDicts:
        combinedString = combineStrings(combinedString, card, width, height)
        width += findWidth(card)

    return combinedString