# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.md
def minSubArrayLen(target: int, nums: list[int]):
    list_length = len(nums)
    left_pointer = 0
    right_pointer = 0
    minimum_len = float('inf')  # 初始化为无穷大
    current_sum = 0  # 当前的累加值

    while right_pointer < list_length:  # the right pointer in the range of the list
        current_sum += nums[right_pointer]  # add the element at the right pointer in the sum

        while current_sum >= target:  # 如果 sum 大于 target
            minimum_len = min(minimum_len, right_pointer - left_pointer + 1)  # update the new minimum length
            current_sum -= nums[left_pointer]  # 从当前总和中减去 'left' 处的元素
            left_pointer += 1  # 将左指针向右移动以缩小窗口

        right_pointer += 1  # 将右指针向右移动以扩大窗口

    return minimum_len if minimum_len != float('inf') else 0


minSubArrayLen(7, [1, 2, 3, 4])
