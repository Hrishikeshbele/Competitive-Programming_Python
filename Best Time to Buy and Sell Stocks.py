'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example :

Input : [1 2]
Return :  1
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, prices):
        profit, min_buy = 0, float('inf')
        #Approach: each day, we evaluate the benefice
        # we get by selling that very day.
        for price in prices:
            min_buy = min(min_buy, price) #is price less than min_buy
            profit = max(profit, price - min_buy)
        return profit
