class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary that contains the array of alphabets as the key and a list of string as the value
        # for each string keep an array of all 26 alphabets
        # check if this already exists as the key in the dictionary
        # if not add the string to the list of for that key
        # return all the values of the dictionary
        dict = defaultdict(list)
        output = []
        for str in strs:
            count = [0] * 26
            for char in str:
                # a = 0
                # b = 1
                index = ord(char)-ord('a')
                count[index] += 1
            dict[tuple(count)].append(str)
        
        for count in dict:
            output.append(dict[count])
        
        return output