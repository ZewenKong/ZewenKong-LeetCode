def generateMatrix(n: int) -> list[list[int]]:

    # 创建了一个 n x n 的二维列表 named "nums", 用于存储最终生成的矩阵, 初始时所有元素都被初始化为 0
    nums = [[0] * n for _ in range(n)]

    # start_x 和 start_y 示当前层次的起始坐标的变量. 起始时, 都设置为0 (表示从矩阵的左上角开始)
    start_x, start_y = 0, 0

    # loop_times 循环次数
    # mid_point 中间点坐标
    loop_times, mid_point = n // 2, n // 2

    
