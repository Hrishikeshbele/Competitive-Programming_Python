
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

idea here is we iterate throght all elms of digits and add letters of next digit to prev combination.
'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        all_comb=[''] if digits else []
        d= {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        #iterate through each digit of digits string
        for digit in digits:
            #create empty list to store combination for this digit with prev all_comb
            curr_comb=[]
            #iterate over each letter of str corrsp to pert digit 
            for letter in d[digit]:
                # add that letter to all elm in prev all_comb this will create our new                       # all_comb list 
                for comb in all_comb:
                    curr_comb.append(comb+letter)
            #updating all_comb list after each iteration
            all_comb=curr_comb
            
        return all_comb
