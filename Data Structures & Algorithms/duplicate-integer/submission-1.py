class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # add numbers to a dictionary as they are looped though
        # check if number is already in dictionary before adding it
        dict = defaultdict(int)

        for num in nums:
            if num in dict:
                return True
            else:
                dict[num] = 1
        return False