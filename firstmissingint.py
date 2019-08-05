'''
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        length = len(A)
        if length == 0:
            return 1
        count = {}
        # marking true for elements in list 
        for i in range(length):
            count[A[i]] = True
        maxElement = max(A)
        #since we need to searh for elm in this range
        for i in range(1,maxElement):
            #if some elment is not present then return it 
            if not count.get(i):
                return i
        #if maxelm is neg return 1
        if maxElement < 0:
            return 1
        #if no elm is missing just return next elm to max elm
        return maxElement + 1
