def rotateString(s, goal):
    """
    :type s: str
    :type goal: str
    :rtype: bool
    """
    if len(s) != len(goal):
        return False

    if len(s) > 0 and len(goal) > 0:
        new_s = s + s
        return (goal in new_s)
    else:
        return False
    