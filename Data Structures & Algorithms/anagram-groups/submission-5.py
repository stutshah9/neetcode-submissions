class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # time complexity: O(n*k) --> k is the maximum length of a string in the input list
        # space complaexity: O(n) --> the dictionary stores references to all n strings
        # for each item in the list create an array with 26 places for each letter in the alphabet
        # loop through each item in the list and increment the count of each character
        # save to a dictionary - append the value to the list associated with the key
        # key = 26 places array
        # value = str associated with 26 place array
        # print the dictionary

        charDict = defaultdict(list)
        result = []
        for word in strs:
            charList = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                charList[idx] += 1
            # list re mutable and therefore cannot be used as dictionary keys
            # use tuple instead because they are immutable
            charDict[tuple(charList)].append(word)
        
        for i in charDict:
            result.append(charDict[i])

        return result


