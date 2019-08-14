'''
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Input: haystack = "hello", needle = "ll"
Output: 2
'''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        for i in  range(len(A)-len(B)+1):
        		#we iterate through string checking for needle from first index to last index
            if A[i:i+len(B)]==B:
                return i
        return -1
            


