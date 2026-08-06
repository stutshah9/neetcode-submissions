class Solution:
    def isValid(self, s: str) -> bool:
        map = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            if char in "{([":
                stack.append(char)
            elif char in "})]":
                if not stack or stack[-1] != map[char]:
                    return False
                stack.pop()
        return len(stack) == 0