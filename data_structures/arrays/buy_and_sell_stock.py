class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0                                        #current max profit 
        minBuy = prices[0]               

        for sell in prices:
            maxP = max(maxP, sell - minBuy)            #find the max between max profit(maxP) stored outside the for loop and the current sell-minBuy
            minBuy = min(minBuy, sell)                 #check if the sell is smaller then the minBuy outside the loop and will update it
        return maxP                                    #return the minBuy, if the minBuy is greater then the sell the maxP will never be updated and return 0
