class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # because it is new repeats use a set
        # add values to the set and check if it already in the set
        charSet = set()

        left = 0

        longestSubstring = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            # after "resetting" the set by removing duplicates and anything preceeding that
            # add the current char to the set
            charSet.add(s[right])
            longestSubstring = max(longestSubstring, len(charSet))

        return longestSubstring
        
