def integerReplacement(n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 1:
            if n & 1 == 0: n >>= 1
            elif n == 3 or n % 4 == 1: n -= 1
            else: n += 1
            count += 1
        return count