def titleToNumber(columnTitle):
    """
    :type columnTitle: str
    :rtype: int
    """
    count = 0
    for x in columnTitle:
        calc = ord(x) - ord('A') + 1
        count = 26 * count + calc
    return count
