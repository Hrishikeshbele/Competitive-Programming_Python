'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        #function to reverse the int 
        def reverse(x):
            n=0
            while x!=0:
                n=n*10+x%10
                x//=10
            return n
        return reverse(x)==x
        
