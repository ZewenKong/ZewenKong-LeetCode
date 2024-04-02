def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    matrix[:] = zip(*matrix[::-1])
    