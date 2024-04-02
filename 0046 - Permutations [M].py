def permute(self):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def backtrack(start):
        if start == len(nums):
            permutations.append(nums[:])
        else:
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

    permutations = []
    backtrack(0)
    return permutations
