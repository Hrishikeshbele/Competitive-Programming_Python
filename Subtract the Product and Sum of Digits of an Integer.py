'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
'''

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        def multiply(x):
            prev=1
            for i in x:
                prev=prev*i
            return prev
        
        x=[int(i) for i in str(n)]
        
        return multiply(x) - sum(x)
