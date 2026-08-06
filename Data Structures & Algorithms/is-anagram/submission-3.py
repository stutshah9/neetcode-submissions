class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # have a dictionary keeping track of each string
        # if the dictionaries are the same at the end, return true
        # if the len of the strings are not the same they are automatically not anagrams
        if len(s) != len(t):
            return False
        
        dicts = defaultdict(int)
        dictt = defaultdict(int)

        for char in s:
            dicts[char] += 1
        
        for char in t:
            dictt[char] += 1
        
        if dicts == dictt:
            return True
        return False