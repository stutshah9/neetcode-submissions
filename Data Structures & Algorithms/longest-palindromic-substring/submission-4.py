class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            # even length
            currLongest = self.evenLength(i, s, longest)

            if len(currLongest) >= len(longest):
                longest = currLongest
                    
            # odd length
            currLongest = self.oddLength(i, s, longest)

            if len(currLongest) >= len(longest):
                longest = currLongest

        return longest
    
    def evenLength(self, i, s, longest) -> str:
        left = i
        right = i + 1
        currLongest = ""

        while (left >= 0 and right < len(s)) and s[left] == s[right]:
            currLongest = s[left] + currLongest + s[right]
            left -= 1
            right += 1
        return currLongest
    
    def oddLength(self, i, s, longest) -> str:
        left = i
        right = i
        currLongest = s[left]
        
        while (left >= 0 and right < len(s)) and s[left] == s[right]:
            left -= 1
            right += 1

            if (left >= 0 and right < len(s)) and s[left] == s[right]:
                currLongest = s[left] + currLongest + s[right]
        return currLongest
        

