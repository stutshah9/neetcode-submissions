class Solution:
    def longestPalindrome(self, s: str) -> str:
        # consider every porition in the string as the center
        # look to the right and left to see if a palindrome is created
        # edge case would be an even length for the palindrome
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l)+1 > resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                l -= 1
                r += 1
            
            # even length palindromes
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l)+1 > resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                l -= 1
                r += 1
        return res
