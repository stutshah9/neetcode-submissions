class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force would be to loop through the nums array twice and check
        # better method: using a dictionary
        # key = num
        # value = index
        dictionary = {}

        for i, num in enumerate(nums):
            if nums[i] in dictionary:
                return True
            
            # add the num into the dictionary
            dictionary[num] = i
        
        return False
