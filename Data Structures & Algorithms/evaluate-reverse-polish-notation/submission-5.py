class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack
        stack = []
        # loop through all the tokens
        for char in tokens:
            # if the token is not an operator add it to the stack
            if char != '+' and char != '-' and char != '*' and char != '/':
                stack.append(int(char))
            # perform the operator
            # add the value back to the stack
            elif char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '-':
                int1, int2 = stack.pop(), stack.pop()
                stack.append(int2 - int1)
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                int1, int2 = stack.pop(), stack.pop()
                stack.append(int(float(int2) / float(int1)))
        
        # return the final value on the stack
        return stack[0]
