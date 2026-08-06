class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set variable to track uniqueness 
        charSet = set()
        # variable to keep track of longest string
        longestString = 0
        # keep track of a left and right variable
        l = 0
        # loop though each char in the string
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longestString = max(longestString, len(charSet))
        return longestString