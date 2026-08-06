class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaString = []
        # loop through the string and every character thats a letter to a array
        for char in s:
            if char.isalnum():
                alphaString.append(char.lower())

        # have 1 pointer at the start of the array and 1 at the end
        i = 0
        j = len(alphaString)-1
        # loop through until the middle to check if every char in the front and end is the same
        while i < j:
            if alphaString[i] == alphaString[j]:
                i += 1
                j -= 1
            else:
                return False

        return True