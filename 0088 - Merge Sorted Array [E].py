print(len([1, 2, 3, 0, 0]))


def mergeSort(nums1, m, nums2, n):
    nums1.extend(nums2)
    nums1.sort()
    for i in range(n):  # from proble discription
        nums1.remove(0)
