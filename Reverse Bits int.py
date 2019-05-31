'''
Reverse bits of an 32 bit unsigned integer and return its value.
Example 1:
x = 0,
          00000000000000000000000000000000  
=>        00000000000000000000000000000000
return 0
'''

class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        #converting given int into 32 bit binary representation
        binary=bin(A)[2:].zfill(32)
        #creating new binary num by flipping all its bits
        new_bin=binary[::-1].zfill(32)
        #returing int value of new binary num
        return int(new_bin,2)
        
