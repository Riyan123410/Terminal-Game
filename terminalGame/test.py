# from asciiArt import asciiHelpers
# from asciiArt import asciiEnemies
# import enemyIntentions


# def formatDescription(description):
#     descriptionList = description.split().copy()
#     line = ""
#     lines = []

#     for i in range(asciiEnemies.DESCRIPTION_HEIGHT):

#         wordsAdded = 0
#         # get each word in the descpription 
#         for word in descriptionList:
#             # add it to the current line if its les than the max len
#             if len(line) + len(word) + 1 < asciiEnemies.DESCRIPTION_LEN:
#                 line += word + " "
#                 wordsAdded += 1
#         # remove all words used
#         for i in range(wordsAdded):
#             descriptionList.pop(0)
        
#         # add spaces until reached max len after add | to finish the line, do -2 for the space and |
#         while len(line) < asciiEnemies.DESCRIPTION_LEN - 2:
#             line += " "
#         line += "|\n"

#         # append each line to the lines list and clear line
#         lines.append(line)
#         line = ""
    
#     return "".join(lines)

# def formatDescriptionList(descriptionList):
#     totalDescriptions = []
#     # loop through the descrption lists and append
#     for description in descriptionList:
#         totalDescriptions.append(formatDescription(description))
#     # join total description list into a string
#     return "".join(totalDescriptions)

# asciiHelpers.displayEnemies()