def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0  # profit on day 1 is 0 because only 1 price is there, meaning that the buy and sell price are the same
    lowest = prices[0]  # on day 1, only one price has been shown which means that it is the lowest
    for i in range(len(prices)):  # iterate through the values in prices
        if prices[i] < lowest:  # if the price at i is less than the lowest value
            lowest = prices[i]  # then set the new lowest value to that price
        if prices[
            i] - lowest > profit:  # if the price at i - the lowest price yields a profit that is greater than the current value of profit
            profit = prices[
                         i] - lowest  # then the value of profit becomes the difference between the price at i and the lowest value
    return profit  # return the profit

# not complete
