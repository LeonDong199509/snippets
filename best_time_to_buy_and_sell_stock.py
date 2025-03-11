class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Brutal force time complexity is O(n^2)
        # The best solution is O(n), with Greedy 
        #     A greedy algorithm makes locally optimal choices at each step with the hope that these choices lead to a globally optimal solution. In this case:
        # 1.	Local Optimal Choice: Always track the lowest price seen so far (the best day to buy).
        # 2.	Greedy Strategy: On each day, compute the potential profit if you were to sell on that day and update the maximum profit.
        # 3.	Global Optimal Solution: By the end of the loop, the algorithm ensures that the best buying and selling days are chosen.
        buy_price = prices[0]
        profit = 0
        for price in prices[1:]:
            profit = max(profit, price - buy_price)
            buy_price = min(price, buy_price)
        
        return profit


        
