class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if left and mid greater than right -> left to mid sorted
        # if left and mid less than right -> left to mid sorted
        # if target is between left and mid -> search on that part
        # else -> search on the other part

        # if right to mid greater than left -> mid to right sorted
        # if right to mid less than lefr -> mid to right sorted
        # if target is between mid and right -> search on that part
        # else -> search on the other part

        left = 0
        right = len(nums) - 1
        while left <= right:

            mid = (right + left) // 2

            if nums[mid] == target:
                return mid

            if (nums[left] > nums[right] and nums[mid] > nums[right]) or (nums[left] < nums[right] and nums[mid] < nums[right]):
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
