class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        LIS = [1] * len(nums)

        # loop that works backwards through every value
        for i in range(len(nums)-1, -1, -1):
            # loop from i through the end of the array
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS)

