class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        # create a dictionary to store each number and the count of each number
        dict = defaultdict(int)
        # the key is the number
        # the value is the count of the number
        for i, num in enumerate(nums):
            dict[num] += 1

        # sort the values in desending order
        sortDict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
        # loop through the first k items and add them to the result list
        for i in range(k):
            result.append(sortDict[i][0])

        return result