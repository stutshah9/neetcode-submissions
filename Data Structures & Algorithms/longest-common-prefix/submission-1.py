class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        shortestStringLen = len(strs[0])
        shortestString = strs[0]
        for s in strs:
            if len(s) < shortestStringLen:
                shortestStringLen = len(s)
                shortestString = s

        # the first string
        tempS = shortestString

        for i in range(shortestStringLen):
            # char i in the first string
            char = tempS[i]

            for s in strs:
                if s[i] != char:
                    return result

            result += char
        
        return result