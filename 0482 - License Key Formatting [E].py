def licenseKeyFormatting(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    s = s.replace('-', '').upper()

    licenseKey = ""
    first = len(s) % k
    for i in range(0, len(s)):
        if i != 0 and (i == first or (i - first) % k == 0):
            licenseKey += "-"
        licenseKey += s[i]
    return licenseKey
