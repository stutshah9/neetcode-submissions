class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # pointer starting at the second location in the list
        # if the num at the pointer is less than the num before the pointer, swap them
        # if you swap once and the value is still smaller than the value to its left swap again
        # keep swapping until that case is no longer true
        # don't move the pointer though use a different pointer to keep track of the swapping
        # otherwise more the pointer to the right by 1
        # repeat this whole thing until the pointer is less than the length of the list

        # pointer = 1
        # this condition takes care of the edge case where there is only 1 value in the list
        # while pointer < len(nums):
        #     prev = pointer - 1
        #     tempPointer = pointer
        #     while prev >= 0 and tempPointer >= 0 and nums[tempPointer] < nums[prev]:
        #         temp = nums[tempPointer]
        #         nums[tempPointer] = nums[prev]
        #         nums[prev] = temp
        #         tempPointer -= 1
        #         prev -= 1
        #     pointer += 1

        # 3 pointer approach
        # use one pointer to keep track of where 0s should be placed
        # another pointer to keep track of where 2s should be placed
        # another pointer to scan through the list
        zero = 0
        two = len(nums) - 1
        curr = 0

        while curr <= two:
            if nums[curr] == 0:
                temp = nums[zero]
                nums[zero] = nums[curr]
                nums[curr] = temp

                zero += 1
                curr += 1
            elif nums[curr] == 2:
                temp = nums[two]
                nums[two] = nums[curr]
                nums[curr] = temp

                two -= 1
            else:
                curr += 1
