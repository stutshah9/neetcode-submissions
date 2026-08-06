class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxCount = 0

        for num in s:
            if num-1 not in s:
                count = 1
                curr = num
                while curr+1 in s:
                    count += 1
                    curr += 1
                maxCount = max(maxCount, count)
        return maxCount

        