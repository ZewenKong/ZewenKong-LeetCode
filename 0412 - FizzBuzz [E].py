def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    output = []

    for i in range(1, n + 1):
        string = ""
        if i % 3 == 0:
            string += "Fizz"
        if i % 5 == 0:
            string += "Buzz"
        if string == "":
            string += str(i)

        output.append(string)
    return output
