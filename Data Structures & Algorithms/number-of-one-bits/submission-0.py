class Solution:
    def hammingWeight(self, n: int) -> int:
        # for the last bit & with all zero's and a one at the last digit
        # shift by 1 to the right
        # loop while n is not zero

        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        
        return count
            