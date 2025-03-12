class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # Still Greedy Solution Time Complexity O(n), Space Complexity O(1)
        buy_price = prices[0]
        profit = 0
        for current_price in prices[1:]:
            if current_price > buy_price:
                profit += current_price - buy_price
            buy_price = current_price
        
        return profit
