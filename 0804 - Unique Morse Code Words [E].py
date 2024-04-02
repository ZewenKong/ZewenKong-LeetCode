def uniqueMorseRepresentations(self, words):
    """
    :type words: List[str]
    :rtype: int
    """
    uniques = set()

    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    for word in words:
        encoded = []
        for char in word:
            index = ord(char) - 97
            encoded.append(morse[index])
        uniques.add("".join(encoded))

    return len(uniques)
