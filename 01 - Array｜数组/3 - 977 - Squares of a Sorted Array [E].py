# 有序数组的平方
# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0977.%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E5%B9%B3%E6%96%B9.md

def squaresOfSortedArray(nums):
    for i in range(len(nums)):
        nums[i] *= nums[i]
    nums.sort()
    return nums
