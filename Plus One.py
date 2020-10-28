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
        if digits[-1]==9 and len(digits)==1: # array have only one elm and it is 9 
            return [1,0]
        if digits[-1]!=9: 
            digits[-1]+=1
            return digits
        else:# when array have more than one 9 at  last in array
            # ex. [2,9,9]. now here in first rectn we will replace last 9 with 0 and pass [2,9] to next recursion here again 9 will be replaced by 0 and we will pass 2 further 
            # which will return 3 so our final output will be [3,0,0]
            #recursively replace last 9 with 0 
            digits[-1]=0
            digits[:-1]=self.plusOne(digits[:-1])
            return digits
