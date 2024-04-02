def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    set1 = set(nums1)
    set2 = set(nums2)

    # set() 把数组变成集合
    # Python 中的集合只储存唯一元素，会把数组内重复的元素删除

    interSection = []

    for i in set1:
        if i in set2:
            interSection.append(i)
    return interSection
