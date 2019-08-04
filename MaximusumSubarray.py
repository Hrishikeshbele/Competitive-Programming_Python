'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        #solution1
        
        def maxSubArray(self, a):
        #Kadane’s Algorithm:You keep accumulating sum till the sum becomes < 0, 
        # at which point you start over again, discarding the accumulated sum.
        maxend,ans=0,-99999
        if len(a)==1:
            return a[0]
        for i in range(len(a)):
            maxend=maxend+a[i]
            if maxend>ans:
                ans=maxend
            if maxend<0:
                maxend=0
        
        return ans
                
            
                
        return ans 
        '''
        #solution2
        for i in range(1,len(nums)):
            #adding prev elm to curr elms
            nums[i]=max(nums[i-1]+nums[i],nums[i])
        return max(nums)
            
