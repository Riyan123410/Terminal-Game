# add a character to the string
def addRowChars(string, legnth, i):
   rowChars = ""
   for j in range(legnth):
       try:
           rowChars += string[i * legnth + j]
       except:
           return "OUT OF RANGE - this shouldnt be seen"
   return rowChars


def combineStrings(string1, len1, string2, len2, height):
   # remove all end lines and create a new string
   string1 = string1.replace("\n", "")
   string2 = string2.replace("\n", "")
   combinedString = ""
   # loop through the height of the strings
   for i in range(height):
       # loop through the legnth of each adding to the new string
       combinedString += addRowChars(string1, len1, i)
       combinedString += addRowChars(string2, len2, i)
       combinedString += "\n"
   return combinedString
