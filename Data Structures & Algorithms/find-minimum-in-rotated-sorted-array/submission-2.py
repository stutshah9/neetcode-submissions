class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        minValue = nums[0]

        while left <= right:
            # if array is sorted
            if nums[left] < nums[right]:
                minValue = min(minValue, nums[left])
                break

            mid = left + ((right-left) // 2)
            minValue = min(minValue, nums[mid])
            
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return minValue
        
