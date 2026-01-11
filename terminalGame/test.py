from asciiArt import asciiEnemies
import enemyIntentions

def formatDescription(description):
    descriptionList = description.split().copy()
    line = ""
    lines = []

    for i in range(asciiEnemies.DESCRIPTION_HEIGHT):

        wordsAdded = 0
        # get each word in the descpription 
        for word in descriptionList:
            # add it to the current line if its les than the max len
            if len(line) + len(word) + 1 < asciiEnemies.DESCRIPTION_LEN:
                line += word + " "
                wordsAdded += 1
        # remove all words used
        for i in range(wordsAdded):
            descriptionList.pop(0)
        
        # add spaces until reached max len after add | to finish the line
        while len(line) < asciiEnemies.DESCRIPTION_LEN:
            line += " "
        line += "|\n"

        # append each line to the lines list
        lines.append(line)
    
    return "".join(lines)
        


def sumChars(lst):
    count = 0
    for string in lst:
        count += len(string)
    return count

print(formatDescription(enemyIntentions.intentionsList["bush"]["turn2"][2]["description"]))
