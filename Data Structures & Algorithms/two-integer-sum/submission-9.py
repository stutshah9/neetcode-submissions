class Solution:
    from collections import defaultdict
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time complexity: O(n^2)
        # space complexity: O(1)
        # loop through the nums array
        # find the difference between the target and the current value
        # from the current index loop to the end of the array
        # if the difference matches the value at the index 
        # append the first and second index to a results list

        # result = []

        # for i in range(len(nums)):
        #     diffrence = target - nums[i]
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == diffrence:
        #             result.append(i)
        #             result.append(j)
        # return result

        # hashmap appraoch
        # save the nums array as a hashmap
        # key = num
        # value = index
        # loop through the array
        # check if the difference is in the hashmap
        numMap = defaultdict(int)
        result = []

        for i in range(len(nums)):
            numMap[nums[i]] = i

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in numMap and numMap[difference] != i:
                result.append(i)
                result.append(numMap[difference])
                return result



        