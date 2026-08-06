class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        stack = []
        # loop though each char in the string
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                stack.pop()
            
            maxDepth = max(maxDepth, len(stack))

        return maxDepth
                