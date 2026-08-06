class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # add any new int into the dictionary
        # check if the difference is already in the dictionary before adding new into to dictionary
        dictionary = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in dictionary:
                return [dictionary[diff], i]
            
            dictionary[num] = i