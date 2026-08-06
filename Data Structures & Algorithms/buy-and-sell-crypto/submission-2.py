class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # base cases would be there is only one price then profit is zero
        # start with pointers on the zero and first index of the array
        # the goal is to find the lowest price to buy and highest price to sell
        # sell cannot be before buy and buy cannot be after sell
        # if buy price is less than sell price calculate the profit
        # if buy price is more than the sell price move buy to sell and move sell to sell + 1 if it exists 

        numPrices = len(prices)
        maxprofit = 0

        if numPrices == 1:
            return 0
        
        buy = 0
        sell = 1
        
        while sell < numPrices:
            if prices[buy] < prices[sell]:
                maxprofit = max(maxprofit, (prices[sell] - prices[buy]))
                sell += 1
            else:
                buy = sell
                sell += 1
        return maxprofit