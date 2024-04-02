# nums = [1, 3, 6, 8]
#
# print(len(nums))
#
# midpoint = 3//2
# print(midpoint)
# print(nums[midpoint])

def serchInsert(nums, target):
    m = 0
    n = len(nums) - 1

    while m <= n:
        midPoint = (m + n) // 2
        if nums[midPoint] == target:
            return midPoint
        elif nums[midPoint] > target:
            n = midPoint - 1
        else:
            m = midPoint + 1

    return n + 1

print(serchInsert([1, 2, 6, 8], 3))
