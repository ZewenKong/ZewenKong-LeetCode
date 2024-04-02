def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    mx_len, start = 0, 0
    used = {}

    for i, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            mx_len = max(mx_len, i - start + 1)
        used[char] = i

    return mx_len
