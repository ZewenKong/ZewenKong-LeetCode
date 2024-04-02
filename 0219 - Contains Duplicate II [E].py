def containsNearbyDuplicate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if len(nums) == len(set(nums)):
        return False
    while any(nums):
        x = nums.pop(0)
        if x in nums:
            if nums.index(x) + 1 <= k:
                return True
    return False

# not complete
