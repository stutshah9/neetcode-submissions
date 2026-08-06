class Solution:
    from collections import defaultdict
    def isAnagram(self, s: str, t: str) -> bool:
        # have 2 dictionaries
        # key = char
        # value = count
        # 1 for string s and 1 for string t
        # loop through both the strings
        # add to the dictionary or increase the count

        dictS = self.dictionaryCreation(s)
        dictT = self.dictionaryCreation(t)

        if dictS != dictT:
            return False
        
        return True

    
    def dictionaryCreation(self, string: str) -> dict:
        length = len(string)
        dictResult = defaultdict(int)
        for i in range(length):
            dictResult[string[i]] += 1

        return dictResult