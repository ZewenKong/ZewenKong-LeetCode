def plusOne(digits):
    string = ""
    for i in digits:
        string += str(i)

    temp = str(int(string) + 1)

    return [int(temp[i]) for i in range(len(temp))]
