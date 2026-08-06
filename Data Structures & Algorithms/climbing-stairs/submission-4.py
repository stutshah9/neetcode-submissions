class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
            
        stepsNeeded = [0] * n
        stepsNeeded[0] = 1
        stepsNeeded[1] = 2

        for i in range(2, n):
            stepsNeeded[i] = stepsNeeded[i-2] + stepsNeeded[i-1]
        
        return stepsNeeded[n-1]