def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    numbers = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }

    n1 = 0
    n2 = 0

    for num in num1:
        n1 = n1 * 10
        n1 += numbers[num]

    for num in num2:
        n2 = n2 * 10
        n2 += numbers[num]

    product = n1 * n2
    result = ""

    while product >= 1:
        rem = product % 10
        for a in numbers:
            if numbers[a] == rem:
                result = a + result
        product = product // 10
    if result == "":
        result = "0"
    return result