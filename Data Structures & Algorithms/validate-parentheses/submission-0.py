class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_open = {')': '(',']': '[','}': '{'}
        for char in s:
            if char in "({[":
                stack.append(char) # push the char onto the stack
            elif char in ")}]":
                # if stack is empty there is nothing to pop out of the stack
                if not stack:
                    return False
                
                top = stack[-1]

                if top != matching_open[char]:
                    return False

                stack.pop()

        return len(stack) == 0