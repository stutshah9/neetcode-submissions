class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
            
        longestSequence = 1

        numbers = set()
        for num in nums:
            numbers.add(num)
        
        for num in nums:
            if (num - 1) not in numbers:
                currentSequence = 1
                while (num + currentSequence) in numbers:
                    currentSequence += 1

                longestSequence = max(longestSequence, currentSequence)
        
        return longestSequence
