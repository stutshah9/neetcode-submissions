import math
class MinStack:

    def __init__(self):
        # the stack stores tuples [val, minVal]
        self.stack = []

    def push(self, val: int) -> None:
        # stack is empty
        if not self.stack:
            self.stack.append([val,val])
        # stack has something in it
        else:
            currentMin = self.stack[-1][1]
            self.stack.append([val, min(currentMin,val)])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
