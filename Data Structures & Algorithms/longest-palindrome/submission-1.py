class Solution:
    def longestPalindrome(self, s: str) -> int:
        # hashmap that stores the count of each character
        # if the values for those keys are divisible by 2
        # add 2 to the result
        # loop through the keys in the hashmap
        # if there is there is any char with an odd count add 1 to the result and break out of the loop

        countDict = defaultdict(int)
        res = 0

        for char in s:
            countDict[char] += 1
            if countDict[char] % 2 ==0:
                res += 2
        
        for cnt in countDict.values():
            if cnt % 2:
                res += 1
                break
        
        return res