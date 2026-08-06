class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through the nums array
        # find the difference between the target and the current value
        # from the current index loop to the end of the array
        # if the difference matches the value at the index 
        # append the first and second index to a results list

        result = []

        for i in range(len(nums)):
            diffrence = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == diffrence:
                    result.append(i)
                    result.append(j)

        return result