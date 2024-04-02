def longestCommonPrefix(strs):

    l = list(zip(*strs))
    # * 将 strs 解包
    # zip, creates tuples, where each tuple contains the characters from the same position in each string.
    # e.g. strs = ["cat", "car", "cab"]
    # [('c', 'c', 'c'), ('a', 'a', 'a'), ('t', 'r', 'b')]

    longestPrefix = ""

    for i in l:
        if len(set(i)) == 1:
            # Check if all elements in the tuple 'i' are the same (using set to find unique elements)
            longestPrefix += i[0]
            # 添加元组里 list 元素的第一个元素
        else:
            break

    return longestPrefix

strs = ["flower","flow","flight"]
print(*strs)

