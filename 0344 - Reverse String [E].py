def reverseString(s):
    s[:] = s[::-1]

    # s[:]
    # 创建 s list 的副本

    # s[::-1]
    # The first colon ':' indicates the start of the slicing operation.
    # The second colon : (followed by -1) indicates the step size of the slicing operation.
    # A step size of -1 means to iterate through the sequence in reverse order.
    # [::-1] specifies that you want to slice the entire sequence,
    # starting from the beginning and moving through it in reverse order,
    # producing a reversed copy of the original sequence.
    