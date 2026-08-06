class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # dictionary
        dict = defaultdict(int)
        # key = alphabet
        # value = count
        left = 0
        longest = 0

        for right in range(len(s)):
            dict[s[right]] += 1
            # find the char that occurs the most
            maxOccurence = max(dict.values())
            if (right-left+1) - maxOccurence > k:
                dict[s[left]] -= 1
                left += 1
            else:
                longest = max(longest, right-left+1)

        return longest


