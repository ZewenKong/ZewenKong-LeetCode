def isPalindrome(s):
    s = s.lower()
    for i in s:
        if not i.isalnum():
            # isalnum() 检查字符串中的所有字符是否都是字母或数字
            s = s.replace(i, "")
    if s == s[::-1]:
        return True
    return False
