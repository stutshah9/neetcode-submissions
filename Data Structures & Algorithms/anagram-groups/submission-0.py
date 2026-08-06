class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # take the alphabet and count how many of each letter there are in the string
        # stored in a hash map where the key is going to be the letters in the alphabet
        # the value is going to the be list of strings with that key
        # if try to access a key that is not present in dict, a new, empty list will be automatically created and associated with that key
        dict = defaultdict(list)

        for s in strs:
            count = [0] * 26    # array for the characters
            for char in s:
                count[ord(char) - ord("a")] += 1
            # for the key (characters in the string)
            # append the value of the string to the values list
            # keys cannot be lists in python so change to tuple 
            # keys must be hasable, and lists are not hashable because they are mutable 
            dict[tuple(count)].append(s)
        return list(dict.values())

        

