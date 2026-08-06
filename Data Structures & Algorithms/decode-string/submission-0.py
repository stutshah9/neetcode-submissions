class Solution:
    def decodeString(self, s: str) -> str:
        # for the entire string
        # push onto a stack until there is a closing bracket
        # when there is a closing bracket pop off the stack until a opening bracket
        # then pop 1 more off the stack to get the number before the bracket
        # then have a loop and a temp string which loops though and adds the temp string that number of times
        
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                temp = ""
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                # pop the opening bracket
                stack.pop()

                # the digit does not have to necessarily be 1 digit it can be multiple
                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                stack.append(int(digit)*temp)
        return "".join(stack)

