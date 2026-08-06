class Solution:
    def trap(self, height: List[int]) -> int:
        # edge case if list is empty
        if not height:
            return 0

        totalWater = 0

        front = 0
        back = len(height)-1

        maxL = height[front]
        maxR = height[back]

        while front < back:
            # if left max is smaller than right max, shift the front
            if min(maxL, maxR) == maxL:
                # update front
                front += 1
                # comapre left max with the current to recompute if needed
                if height[front] > maxL:
                    maxL = height[front]
                # the left max is updated before water is calculated so water will never be 0 therefore check is not required
                totalWater += maxL - height[front]

            # if right max is smaller than left max, shift the back
            elif min(maxL, maxR) == maxR:
                # update back
                back -= 1
                # compare right max with the current to recompute if needed
                if height[back] > maxR:
                    maxR = height[back]

                totalWater += maxR - height[back]
        return totalWater