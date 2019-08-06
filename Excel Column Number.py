'''
Given a column title as appears in an Excel sheet, return its corresponding column number.

Example:

    A -> 1
    
    B -> 2
    
    C -> 3
    
    ...
    
    Z -> 26
    
    AA -> 27

'''

class Solution:
    # @param A : string
    # @return an integer 
    def titleToNumber(self, A):
        ans=0
        #using ord value we are calculating col number,since A start from 65 we are sub 64 from each char
        for i in (A):
            ans=ans*26+(ord(i) - 64)
        return ans
