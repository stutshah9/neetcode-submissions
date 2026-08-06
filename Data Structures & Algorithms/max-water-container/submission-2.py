class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointers one at the front and one at the back
        front = 0
        back = len(heights)-1

        maxArea = 0

        # calculate the area
        while front < back:
        # min(heights[front], heights[back])*(back-front)
            area = min(heights[front], heights[back])*(back-front)
            if maxArea < area:
                maxArea = area
        # move the pointer with the smaller height to potentially reduce height bottle neck
            minHeight = min(heights[front], heights[back])
            if minHeight == heights[front]:
                front += 1
            else:
                back -= 1
        return maxArea

