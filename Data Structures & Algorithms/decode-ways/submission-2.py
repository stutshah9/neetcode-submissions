class Solution:
    def numDecodings(self, s: str) -> int:
        # dp approach
        # loop through the numbers one at a time
        # use the digit alone - if the number is a single digit from 1-9 add dp[i-1] to dp[i]
        # use the digit with another - if the number two digit number is between 10 and 26 add dp[i-2] to dp[i]
        
        if s[0] == '0':
            return 0
        
        if len(s) == 1:
            return 1
        
        dp = [0] * (len(s) + 1)
        
        dp[0] = 1 # dummy/base case that makes the recurrence work cleanly
        dp[1] = 1 # 1st digit
        # dp[i] represents the number of ways for the i-1 digit to be represented
        for i in range(2, len(s) + 1):
            # current single digit
            if s[i - 1] != "0":
                dp[i] += dp[i-1]
            
            # previous two digits
            if "10" <= s[i-2] + s[i - 1] <= "26":
                dp[i] += dp[i-2]
        
        return dp[len(s)]