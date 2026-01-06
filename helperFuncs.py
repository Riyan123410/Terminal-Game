def clamp(num, minNum, maxNum):
    if num < minNum:
        return minNum
    if num > maxNum:
        return maxNum
    return num

# change and clamp
def changeWithClamp(num, change, minNum, maxNum):
    return clamp(num + change, minNum, maxNum)