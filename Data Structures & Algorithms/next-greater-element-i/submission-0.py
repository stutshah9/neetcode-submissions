class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create dictionary
        dict = defaultdict(int)
        for i, num in enumerate(nums1):
            dict[num] = i
        
        stack = []
        res = [-1]*len(nums1)

        for i in range(len(nums2)):
            # check to see if the current num is greater than all the items in the stack
            while stack and nums2[i] > stack[-1]:
                number = stack.pop()
                res[dict[number]] = nums2[i]
            # add the current number to the stack if it exists in nums1
            if nums2[i] in dict:
                stack.append(nums2[i])
        return res
            