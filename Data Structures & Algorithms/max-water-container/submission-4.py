class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointers, one at the end and one at the start
        # the bottle neck for the height of the water is the shorter bar
        # move the left and right pointer by checking which bar is shorter
        left = 0
        right = len(heights)-1

        maximum = 0

        while left < right:
            height = min(heights[left], heights[right])
            width = right-left

            area = height*width

            maximum = max(maximum, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maximum