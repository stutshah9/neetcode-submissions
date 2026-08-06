class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [char, count]
        # loop through string
        for char in s:
        # add each character to the stack
        # keep count of how many times that character has occured - can do this by using pairs of values
        # check the top character to see if it is the same
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
        # as soon as the count of a character at the top of the stack is equal to k
            if stack[-1][1] == k:
                # remove that character (pop from stack)
                stack.pop()
        # return the stack
        result = ""
        for char,count in stack:
            result += (char * count)
        
        return result