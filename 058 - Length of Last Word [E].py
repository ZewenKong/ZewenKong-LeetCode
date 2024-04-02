# s = "Hello World"
#
# ss = s.split()
#
# print(ss)

def lengthOfLastWord(s):
    return len(s.split()[-1])
    # 根据指定的分隔符将字符串拆分为子字符串列表
    # 如果未指定分隔符，该方法将默认按空白（空格、换行符等）进行分割

    # Syntax: string.split(separator, maxsplit)
    # separator (optional): The delimiter according to which the string is split. If not provided, the string is split on whitespace.
    # maxsplit (optional): Defines the maximum number of splits. The default (-1) means no limit.

    # Example
    # Without a separator: 'a b c'.split() would result in ['a', 'b', 'c'].
    # With a separator: 'a,b,c'.split(',') would result in ['a', 'b', 'c'].
    # With maxsplit: 'a b c'.split(' ', 1) would result in ['a', 'b c'].


print(lengthOfLastWord("Hello World"))
