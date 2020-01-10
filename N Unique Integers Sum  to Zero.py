'''
Given an integer n, return any array containing n unique integers such that they add up to 0.
solution approach:start with -(n-1) and append the integer with gap of 2 upto n.which eventually will give us array whose sum is 0.
'''

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return range(1-n,n,2)
