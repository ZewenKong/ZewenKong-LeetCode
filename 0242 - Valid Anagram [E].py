def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # s = list(sorted(s))
    # t = list(sorted(t))
    s = sorted(s)
    t = sorted(t)
    return s == t


# s = "anagram"
# print(sorted(s))
# print(list(sorted(s)))
# t = "nagaram"