# Palindrome Number 回文数
def isPalindrome(num):
    return str(num) == str(num)[::-1]


# str(num) 将整数 num 转换成字符串
# str(num)[::-1] 逆字符串

print(isPalindrome(121))

print(isPalindrome(123))
