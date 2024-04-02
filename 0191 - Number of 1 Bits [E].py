def hammingWeight(self, n: int) -> int:
    # Initialize a variable 'ans' to store the count of set bits.
    ans = 0

    # Continue looping as long as 'n' is not equal to 0.
    while n:
        # Check if the least significant bit (LSB) of 'n' is 1.
        # To do this, we use 'n % 2', which gives us the remainder when 'n' is divided by 2.
        # If 'n % 2' is 1, it means the LSB is 1, so we increment 'ans' by 1.
        ans += n % 2

        # Right-shift 'n' by one bit by performing integer division by 2.
        # This effectively removes the processed LSB, and the next bit
        # becomes the new LSB in the next iteration.
        n //= 2

    # Return the final count of set bits stored in 'ans'.
    return ans

# Not complete