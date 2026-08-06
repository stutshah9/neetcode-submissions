class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # while left pointer is less than right pointer
        # find the middle of the list
        # check if the target is less than or greater than the middle
        # if it is less than search the bottom half
        # if it is greater than serach the top half
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + ((right - left)//2)

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

