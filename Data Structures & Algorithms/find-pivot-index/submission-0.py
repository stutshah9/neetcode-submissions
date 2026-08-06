class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0] * len(nums)
        postfixSum = [0] * len(nums)

        presum = 0
        postsum = 0

        for i in range(len(nums)):
            presum += nums[i]
            prefixSum[i] = presum
        
        for i in range(len(nums) - 1, -1, -1):
            postsum += nums[i]
            postfixSum[i] = postsum
        
        index = 0
        while index < len(nums):
            if prefixSum[index] == postfixSum[index]:
                return index
            else:
                index += 1
        
        return -1
