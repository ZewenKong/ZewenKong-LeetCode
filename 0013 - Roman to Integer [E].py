def romanToInt(testValue):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }


    testValue = testValue.replace("IV", "IIII").replace("IX", "IIIIIIIII")

    testValue = testValue.replace("XL", "XXXX").replace("XC", "XXXXXXXXX")

    testValue = testValue.replace("CD", "CCCC").replace("CM", "CCCCCCCCC")

    intValue = 0

    for char in testValue:  # 循环遍历每个字符
        intValue += roman_dict[char]
        # Access the dictionary roman_dict
        # This dictionary maps individual Roman numeral characters to their corresponding integer values.
        # For example, roman_dict['I'] would return 1, roman_dict['V'] would return 5, and so on.

    return intValue


# Test

testValue = "MCMXCIV"

print(romanToInt(testValue))
