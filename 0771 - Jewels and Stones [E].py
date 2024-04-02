def numJewlsInStones(jewels: str, stones: str):
    # return sum(stones.count(j) for j in jewels)
    count = 0

    for i in range(len(stones)):
        if stones[i] in jewels:
            count += 1
    return count
