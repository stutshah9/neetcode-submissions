class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # use a dictionary
        dict1 = {}
        dict2 = {}

        # have the key being the character
        # the value should be the count
        # do this for string s and t
        for i, char in enumerate(s):
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        
        for i, char in enumerate(t):
            if char in dict2:
                dict2[char] += 1
            else:
                dict2[char] = 1
                     
        # see if both the dictionaries produced are the same
        if dict1 == dict2:
        # if they are the same return true
            return True
        # or else return false
        else:
            return False