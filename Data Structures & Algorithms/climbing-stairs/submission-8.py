class Solution:
    def climbStairs(self, n: int) -> int:
        # time complexity: O(n)
        # space compaxity: O(n)
        # every way of reaching stair i - 2 can be extended by two steps and every way of reaching step i - 1 can be extended by one step
        
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