class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        # use a prefix and post fix array to store the product
        # prefix array
        prefix = 1
        prefixArray = []
        for i in nums:
            prefix *= i
            prefixArray.append(prefix)
        
        # postfix
        postfix = 1
        postfixArray = [1] * len(nums)
        for i in range(len(nums)-1,-1, -1):
            postfix *= nums[i]
            postfixArray[i] = postfix

        # multiply the i-1 prefix with the i+1 postfix to get the final value
        for i in range(len(nums)):
            multiply = 1
        # edge cases: first and last position of the array
            if i == 0:
                multiply = postfixArray[i+1]
            elif i == len(nums) - 1:
                multiply = prefixArray[i-1]
            else:
                multiply = prefixArray[i-1] * postfixArray[i+1]
            output.append(multiply)

        return output