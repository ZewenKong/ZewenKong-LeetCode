from collections import defaultdict

def mostCommonWord(paragraph: str, bannedWord: list[str]):
    for i in "!.',;:?":
        paragraph = paragraph.replace(i, ' ')
        # 遍历所有的标点符号，将段落中的标点符号替换为空格，以便后续分词。

    dic, ans, ansCount = defaultdict(int), '', 0
    # 初始化一个字典dic来记录每个单词的出现次数，默认值为0；初始化ans为最终答案的单词，初始化ansCount为这个单词的出现次数。

    for word in paragraph.lower().split():
        # 将段落转换为小写并分割成单词列表，遍历每个单词。

        if word in bannedWord:
            continue
        # 如果当前单词在禁止列表中，跳过这个单词的处理。

        dic[word] += 1
        # 如果单词不在禁止列表中，将其出现次数加一。

        if dic[word] > ansCount:
            ansCount = dic[word]
            ans = word
        # 如果当前单词的出现次数大于已记录的最大出现次数，更新最大出现次数和对应的单词。

    return ans
    # 返回出现次数最多的单词。
