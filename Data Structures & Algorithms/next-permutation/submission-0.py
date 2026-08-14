class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force approach: find all the permutations in sorted order, find the current permutation, result will be the next one or loop around to the start

        # two pointer approach
        pivot = len(nums) - 2
        largest = len(nums) - 1

        # find the first number that is not in ascending order from the right (pivot)
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        if pivot >= 0:
            # find the number to the right of the pivot that is larger than the pivot from the right
            while largest > pivot and nums[largest] <= nums[pivot]:
                largest -= 1

            # swap those numbers
            temp = nums[largest]
            nums[largest] = nums[pivot]
            nums[pivot] = temp

        # reverse from the pivot point to the right
        left = pivot + 1
        right = len(nums) - 1

        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
