class Solution:
    def isValid(self, s: str) -> bool:
        # hash map (dictionary) to store the pairs of parentheses
        parenDict = {')': '(', '}': '{', ']': '['}
        # stack to push open parenthese and pop open parentheses if a closed parentheses match is found
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if stack and stack[-1] == parenDict[char]:
                    stack.pop()
                else:
                    return False
        # if stack is empty at the end return true
        if len(stack) == 0:
            return True
        # else return false
        else:
            return False
    