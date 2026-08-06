class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        maxProfit = 0

        while left < right and right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                maxProfit = max(maxProfit, prices[right]-prices[left])
            right += 1

        return maxProfit
        
            