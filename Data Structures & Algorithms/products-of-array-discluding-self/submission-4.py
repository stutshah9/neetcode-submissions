class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1] * len(nums)
        sufixProduct = [1] * len(nums)

        result = [1] * len(nums)

        for i in range(1, len(nums)):
            prefixProduct[i] = prefixProduct[i-1] * nums[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            sufixProduct[i] = sufixProduct[i+1] * nums[i+1]

        for i in range(len(nums)):
            result[i] = prefixProduct[i] * sufixProduct[i]
        
        return result