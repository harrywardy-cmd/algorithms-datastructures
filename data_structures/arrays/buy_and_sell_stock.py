class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Tracks the maximum profit found so far
        maxP = 0

        # Lowest stock price seen so far (best day to buy)
        minBuy = prices[0]

        # Iterate through each stock price as a potential selling price
        for sell in prices:

            # Calculate profit if we sell today using the
            # lowest purchase price seen so far
            maxP = max(maxP, sell - minBuy)

            # Update the lowest buying price if a cheaper
            # stock price is found
            minBuy = min(minBuy, sell)

        # Return the highest profit possible
        return maxP
