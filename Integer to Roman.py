'''
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"

'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans=''
        strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]        
        for i,val in enumerate(nums):
            #we will enter in while loop when corrs val in nums is just less than num and 
            # num value will decrease until number become less than than curr val then
            # we will again go in for loop search for closest val in nums that is just 
            # less than curr num and this process will repeat
            while num>=val:
                ans+=strs[i]
                num-=val

        return ans
        
