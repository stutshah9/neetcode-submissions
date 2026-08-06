class Solution:

    def encode(self, strs: List[str]) -> str:
        # loop through the list of strings
        # for each string in the list get the length
        # append the length of the string to an results list
        # after appending the length append a '#' char
        # then append the string
        # use "".join(strs) to join the results list into a string
        # return the joint string
        results = []
        for string in strs:
            results.append(str(len(string)))
            results.append('#')
            results.append(string)
        
        return "".join(results)

    def decode(self, s: str) -> List[str]:
        # while not at end of string
        # get the number from the start of the word
        # skip the '#'
        # grab the next couple letters according to the size
        # append those to the results
        # move the counter to the next size

        results = []
        counter = 0
        while counter < len(s):
            char = counter
            while s[char] != '#':
                char += 1
            size = int(s[counter : char])
            counter = char
            word = s[counter + 1 : counter + 1 + size]
            results.append(word)
            counter = counter + 1 + size
        
        return results
