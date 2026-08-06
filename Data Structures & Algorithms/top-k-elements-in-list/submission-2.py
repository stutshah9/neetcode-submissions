class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary to keep track of what numbers occur and how many
        dict = {}
        output = []
        # loop though the nums list
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        # sort the dict in decending order to get the first k most frequent numbers
        # using sorted builds a list of tuples
        sortedDict = sorted(dict.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            output.append(sortedDict[i][0])
        
        return output
