def addBinary(self, a, b):
    x, y = int(a, 2), int(b, 2)
    # int(a, 2)
    # transfer x to decimal

    return str(bin(x + y).replace("0b", ""))
    # bin(x+y)
    # transfer to binary
    # .replace("0b","")
    # delete 0b (change 0b to empty string)
