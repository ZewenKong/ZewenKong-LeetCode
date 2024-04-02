
# Method 1: Loop though the whole list
def two_sum(nList, tValue):
    dic = {}
    for i in range(len(nList)):  # loop through number in the list
        if tValue - nList[i] in dic:  # target minus the number
            return [dic[tValue - nList[i]], i]
            # return the place of the value (first argument), and the place of current number
            # Hint: dictionary[1] ==> the item with key '1'
        else:
            dic[nList[i]] = i
            # the value save as 'key', the order save as 'item'


# Test value
numberList = [2, 7, 11, 15]
targetValue = 9
print(two_sum(numberList, targetValue))


# Method 2: Hash map
# ...