# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.md

def binarySearch(self, nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if nums[middle] > target:
            right = middle - 1  # target在左区间，所以[left, middle - 1]
        elif nums[middle] < target:
            left = middle + 1  # target在右区间，所以[middle + 1, right]
        else:
            return middle
    return -1  # 未找到目标值


