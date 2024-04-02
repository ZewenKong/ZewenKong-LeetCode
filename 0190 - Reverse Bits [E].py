# @param n, an integer
# @return an integer
def reverseBits(n):
    return int((bin(n).replace("0b", "").rjust(32, "0"))[::-1], 2)
