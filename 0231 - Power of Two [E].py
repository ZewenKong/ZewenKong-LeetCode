def isPowerOfTwo(num: int):
    if num == 1:
        return True

    x = 2

    while x <= num:
        if x == num:
            return True
        x *= 2
    return False
