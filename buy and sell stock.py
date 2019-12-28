'''
problem link- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf')
        for price in prices:
            #find min price among current price and existing min price
            min_price=min(price,min_price)
            max_profit=max(max_profit,price-min_price)
        return max_profit
