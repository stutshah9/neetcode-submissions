class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numDict = defaultdict(int)
        result = []
        for num in nums:
            numDict[num] += 1
        
        for i in range(1, len(nums) + 1):
            if numDict[i] == 0:
                result.append(i)
        
        return result
