class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # using a prefix sum
        # using a hashmap to store the prefix sums acheived so far during the iteration
        prefixDict = defaultdict(int)
        prefixDict[0] = 1
        sum = 0
        result = 0
        for num in nums:
            sum += num
            difference = sum - k
            if difference in prefixDict:
                result += prefixDict[difference]

            prefixDict[sum] += 1
        
        return result

