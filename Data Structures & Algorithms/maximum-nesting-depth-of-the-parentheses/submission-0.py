class Solution:
    def maxDepth(self, s: str) -> int:
        # declare a stack
        stack = []
        # maximum variable keeping track of the max depth
        maxDepth = 0
        # loop through each char in the string
        for char in s:
        # if the char is "(" append it to the stack
            if char == '(':
                stack.append(char)
        # if the char is ")" pop of the stack
            elif char == ")":
                stack.pop()
            else:
                continue
        # if maxDepth < current depth of the stack
            if maxDepth < len(stack):
        # maxDepth = current depth of the stack
                maxDepth = len(stack)
        # return the max depth
        return maxDepth