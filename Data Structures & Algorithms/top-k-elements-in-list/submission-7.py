class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # the input is not necessarily sorted
        # loop through all the nums in the string
        # create a dictionary with the values of the num and the count
        # key = num
        # value = count
        # sort the values in the dictionary in descending order
        # add the first k to the result list

        result = []
        numDict = defaultdict(int)

        for num in nums:
            numDict[num] += 1
        
        sortedNumDict = dict(sorted(numDict.items(), key=lambda item: item[1], reverse=True))

        print(sortedNumDict)

        count = 1
        for num in sortedNumDict:
            if count <= k:
                result.append(num)
                count += 1
        
        return result
        