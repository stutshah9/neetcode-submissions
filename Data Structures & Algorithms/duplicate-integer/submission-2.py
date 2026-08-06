class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # have a set which contains seen values
        # loop through the list
        # if the value is already in the set output true
        # else output false

        numSet = set()
        length = len(nums)
        for i in range(length):
            if nums[i] not in numSet:
                numSet.add(nums[i])
            else:
                return True
        
        return False
