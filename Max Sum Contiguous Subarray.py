'''
Find the contiguous subarray within an array, A of length N which has the largest sum.
Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output 2:
    6

Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6.
    
idea is here to keep track of max sum upto each index and at each index we have to option either start new subarray from curr elm or continue prev array with adding curr elm. we 
see which one has max sum and we keep that. we use one variable to keep track of max sum .

'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, a):
        #Kadane’s Algorithm:
        maxend,currsum=a[0],-9999
        for i in range(len(a)):
            currsum=max(a[i],currsum+a[i])
            maxend=max(maxend,currsum)
        
        return maxend
                
            
        
