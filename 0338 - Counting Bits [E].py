def countBits(n):
    # Initialize a list to store the counts of set bits for each number.
    counter = [0]

    # Loop through numbers from 1 to n (inclusive).
    for i in range(1, n + 1):
        # To count the set bits for 'i', we use the value at counter[i >> 1]
        # which represents the count of set bits in 'i' after removing its
        # least significant bit (right shift by 1). We also add 'i % 2' to
        # consider the least significant bit, which is either 0 or 1.
        # This way, we accumulate the count of set bits for 'i'.
        counter.append(counter[i >> 1] + i % 2)

    # Return the list of counts for each number from 0 to n.
    return counter

# not complete