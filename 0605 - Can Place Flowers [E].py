def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    empty_or_not = 1
    flowerbeds_count = 0
    for bed in flowerbed:
        if bed:
            flowerbeds_count += (empty_or_not - 1) // 2
            empty_or_not = 0
        else:
            empty_or_not += 1

    flowerbeds_count += empty_or_not // 2

    planted_or_not = flowerbeds_count >= n

    return planted_or_not