class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i,len(prices)):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit,profit)
        # return max_profit

        max_profit = 0
        left=0
        right = 1

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right]-prices[left]
                max_profit = max(profit,max_profit)
            else:
                left=right
            right = right + 1
        return max_profit






                
        