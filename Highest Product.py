'''
Given an array of integers, return the highest product possible by multiplying 3 numbers from the array.
[0, -1, 3, 100, 70, 50]

=> 70*50*100 = 350000
'''
#It is always max of(smallest two negative digits and biggest positive or last three big positive numbers)

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        if len(A)<3:
            return -1
        A.sort()
        return max(A[-1]*A[0]*A[1],A[-1]*A[-2]*A[-3])
