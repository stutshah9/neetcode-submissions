class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary of key-value pairs
        # key is the num
        # index is the value
        dictionary = {}

        # loop though the array
        # get the index and num value
        for i, num in enumerate(nums):
            # calculate the difference between the the target and current number
            diff = target - num

            if diff in dictionary:
                return [dictionary[diff], i]

            # adding to the dictionary after deals with picking the current number as both the differnce and i
            dictionary[num] = i
