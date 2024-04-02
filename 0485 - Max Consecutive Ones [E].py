def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    consecutive = 0
    result = 0

    for i in nums:
        if i:
            consecutive += 1
        else:
            result = max(consecutive, result)
            consecutive = 0
    return max(consecutive, result)
