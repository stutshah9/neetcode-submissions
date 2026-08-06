class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # height is a constraint
        # max right and max left of the current index is needed
        left = 0
        right = len(height)-1

        maxRight = height[right]
        maxLeft = height[left]

        countWater = 0
        # whichever one is smaller between max right and max left, the pointer on that side needs to move
        # at the current moment only min(MR, ML) - current height water can be filled
        while left < right:
            if maxLeft <= maxRight:
                left += 1
                # update max left if needed
                maxLeft = max(maxLeft, height[left])
                countWater += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                countWater += maxRight - height[right]

        return countWater
        
        