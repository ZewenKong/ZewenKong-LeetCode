def climbStairs(n):
    if n <= 2:
        return n

    # is placed below the if statements in the climbing stairs problem is due to
    # efficiency and the handling of base cases.

    dp = [0] * (n + 1)
    # a list named dp with a length of n + 1.
    # where each element is set to 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
