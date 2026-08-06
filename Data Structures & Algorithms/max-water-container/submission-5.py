class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAreaReturn = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            if heights[left] <= heights[right]:
                area = heights[left] * (right - left)
                maxAreaReturn = max(maxAreaReturn, area)
                left += 1
            else:
                area = heights[right] * (right - left)
                maxAreaReturn = max(maxAreaReturn, area)
                right -= 1

        return maxAreaReturn