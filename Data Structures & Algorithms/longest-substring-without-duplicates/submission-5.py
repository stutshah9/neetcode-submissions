class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        charSet = set()
        left = 0
        right = 1

        maxLength = 1

        charSet.add(s[left])

        while right < len(s):
            if s[right] not in charSet:
                charSet.add(s[right])
                right += 1
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
                right += 1

            maxLength = max(maxLength, right - left)

        return maxLength