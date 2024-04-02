def convertToTitle(columnNumber):
    """
    :type columnNumber: int
    :rtype: str
    """
    ans = ""

    while columnNumber > 0:
        columnNumber -= 1
        # Get the last character and append it at the end of the string.
        ans += chr(columnNumber % 26 + ord('A'))
        columnNumber //= 26

    # Reverse it, as we appended characters in reverse order.
    ans = ans[::-1]
    return ans

# Not complete
