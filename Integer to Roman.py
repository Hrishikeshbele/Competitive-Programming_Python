'''
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"

idea here is first create 2 list 1st contains roman letters and second containing corrsp values.then we loop through val's list and compare
each elm in it with given num if we find that num is just greater than curr elm we enter into while loop in which we first add roman letter
corresponding curr val to ans then substract curr val from num and again check if it is greater than curr val if not we proceed with for 
loop with updated num val this process repeats
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
        
