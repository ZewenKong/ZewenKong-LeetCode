def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    l1 = list(s)
    l2 = list(t)

    for i in l2:
        if i in l1:
            l1.remove(i)
        else:
            return i
