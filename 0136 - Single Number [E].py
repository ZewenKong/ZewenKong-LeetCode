# def singleNumber(nums: list[int]):
#     for i in nums:
#         if nums.count(i) == 1:
#             return i

# def singleNumber(nums: list[int]):
#     return 2 * sum(set(nums)) - sum(nums)

def singleNumber(nums: list[int]) -> list[int]:

    single_numbers = []

    for i in nums:
        if nums.count(i) == 1:
            single_numbers.append(i)
    return single_numbers


nums = [0, 1, 2, 3, 3, 4, 4, 5, 5]
print(singleNumber(nums))
