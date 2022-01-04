def swapPositions(myList, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
myList = [12, 34, 45, 56]
pos1, pos2 = 1, 2
print(swapPositions(myList, pos1 - 1, pos2 - 1))