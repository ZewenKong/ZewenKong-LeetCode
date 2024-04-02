def majorityElement(nums: list[int]):
    nums.sort()
    return nums[len(nums) // 2]
