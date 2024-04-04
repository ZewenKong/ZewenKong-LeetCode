def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    while (len(str(num)) > 1):
        temp = 0
        for x in str(num):
            temp += int(x)
        
        num = temp
        if len(str(num)) == 1:
            break
    
    return(num)
