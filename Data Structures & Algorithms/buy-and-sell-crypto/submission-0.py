class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use 2 pointers starting at the first 2 locations
        pointer1 = 0
        pointer2 = 1

        # max profit variable
        maxProfit = 0

        # while r < len(prices)
        while pointer2 < len(prices):
        # if the price of the first pointer is less than the price of the second counter
            if prices[pointer1] < prices[pointer2]:
        # calculate the profit
                profit = prices[pointer2] - prices[pointer1]
        # if profit is more than current max profit make max profit the new profit
                maxProfit = max(profit, maxProfit)
        # since second pointer is smaller than the first pointer
        # the value of the second pointer should become the value of the first pointer
            else:
                pointer1 = pointer2
        # the value of the second pointer must be after the first pointer therefore add one in the else case
        # or add one for a potential larger profit in the if case
            pointer2 += 1

        return maxProfit
