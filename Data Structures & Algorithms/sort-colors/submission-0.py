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

        pointer = 1
        # this condition takes care of the edge case where there is only 1 value in the list
        while pointer < len(nums):
            prev = pointer - 1
            tempPointer = pointer
            while prev >= 0 and tempPointer >= 0 and nums[tempPointer] < nums[prev]:
                temp = nums[tempPointer]
                nums[tempPointer] = nums[prev]
                nums[prev] = temp
                tempPointer -= 1
                prev -= 1
            pointer += 1

        