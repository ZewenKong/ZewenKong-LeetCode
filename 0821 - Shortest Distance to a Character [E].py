def shortestToChar(s, c):
    """
    :type s: str
    :type c: str
    :rtype: List[int]
    """
    lengthOf_string = len(s)
    result = [lengthOf_string] * lengthOf_string
    lastItem_string = -lengthOf_string
    for i in list(range(lengthOf_string)) + list(range(lengthOf_string)[::-1]):
        if (s[i] == c):  lastItem_string = i
        result[i] = min(result[i], abs(i - lastItem_string))
    return result
