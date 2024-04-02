def pascalSTriangle(numRows: int):
    finalList = []
    finalList.append([1])

    for i in range(numRows - 1):
        newList = [1]
        for j in range(i):
            newList.append(finalList[i][j] + finalList[i][j + 1])
        newList.append(1)
        finalList.append(newList)
    return finalList
