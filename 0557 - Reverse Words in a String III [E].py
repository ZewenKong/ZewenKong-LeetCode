def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    ss = s.split(' ')

    for i in range(len(ss)):
        ss[i] = ss[i][::-1]
    return ' '.join(ss)
