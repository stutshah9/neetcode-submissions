class Solution:
    def longestPalindrome(self, s: str) -> str:
        bestStart = 0
        bestLength = 0

        for i in range(len(s)):
            # even length
            length, start = self.evenLength(i, s)

            if length > bestLength:
                bestStart = start
                bestLength = length
                    
            # odd length
            length, start = self.oddLength(i, s)

            if length > bestLength:
                bestStart = start
                bestLength = length

        return s[bestStart : bestStart + bestLength]
    
    def evenLength(self, i, s) -> str:
        left = i
        right = i + 1
        
        bestStart = i
        bestLength = 0

        while (left >= 0 and right < len(s)) and s[left] == s[right]:
            currentLength = right - left + 1

            if currentLength > bestLength:
                bestStart = left
                bestLength = currentLength

            left -= 1
            right += 1

        return bestLength, bestStart
    
    def oddLength(self, i, s) -> int:
        left = i
        right = i

        bestStart = i
        bestLength = 1
        
        while (left >= 0 and right < len(s)) and s[left] == s[right]:
            currentLength = right - left + 1

            if currentLength > bestLength:
                bestStart = left
                bestLength = currentLength

            left -= 1
            right += 1

        return bestLength, bestStart
