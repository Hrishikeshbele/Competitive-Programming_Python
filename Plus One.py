'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1]==9 and len(digits)==1:
            return [1,0]
        if digits[-1]!=9:
            digits[-1]+=1
            return digits
        else:
            #recursively replace last 9 with 0 
            digits[-1]=0
            digits[:-1]=self.plusOne(digits[:-1])
            return digits
