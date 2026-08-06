class Solution:
    def isValid(self, s: str) -> bool:
        # use a dictionary
        # value = the open parentheses
        # key = the closed parentheses
        # use a stack to push the characters if they are an open parentheses
        # if it is a closed parentheses it should be the pair of the open parentheses

        parenthesesDict = {')' : '(', ']' : '[', '}' : '{'}
        stack = []
        counter = 0
        if len(s) == 1:
            return False

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
                counter += 1
            else:
                if counter == 0:
                    return False
                elif stack[-1] == parenthesesDict[char]:
                    stack.pop()
                    counter -= 1
                else:
                    return False
        if counter == 0:
            return True
        else:
            return False