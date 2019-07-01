'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return 1 ( true ).
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, nums):
        m = 0 #The largest index that can be reached
        for i, n in enumerate(nums):
            #when the current position can not reach next position(when m<=i or A[i]==0)
            # max<=i means that we've reached the last accessible node - cannot jump further, 
            #and current value is 0, meaning that if we do jump on that step, we'll stay there.
            if i > m:
                return 0
            m = max(m, i+n)
        return 1
            
