class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack in this case keeps track of char, count
        stack = [] # char, count

        # loop though the whole string
        for char in s:
        # check if the count for the last value in the stack is < k
        # if it is increment the value of k
        # or else pop the char of the stack
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char,1])
            
            if stack[-1][1] == k:
                stack.pop()

        result = ""
        for char, count in stack:
            result += (char * count)
        
        return result
