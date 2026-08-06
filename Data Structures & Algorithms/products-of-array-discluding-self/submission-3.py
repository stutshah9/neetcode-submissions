class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and post fix array
        # prefix array holds the sum of each num from the beginning
        # postfix array holds the sum of each num fron the end
        output = []

        prefixArray = []
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            prefixArray.append(product)
        
        postfixArray = [0]*len(nums)
        product = 1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            postfixArray[i] = product
        
        for i in range(len(nums)):
            if i == 0:
                output.append(postfixArray[i+1])
            elif i == len(nums)-1:
                output.append(prefixArray[i-1])
            else:
                output.append(prefixArray[i-1] * postfixArray[i+1])
        return output

            

