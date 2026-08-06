class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actualResult = 0
        predResult = 0

        n = len(nums)

        for num in nums:
            actualResult = actualResult ^ num
        
        for i in range(n+1):
            predResult = predResult ^ i
        
        return predResult ^ actualResult