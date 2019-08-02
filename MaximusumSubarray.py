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
        if len(nums)==1:
            return nums[0]
        ans=-999999
        for start in range(len(nums)):
            n=0
            #iterate for diff sizes of arrays
            for size in range(1,len(nums)+1):
                if size+start>len(nums):
                    break
                n+=nums[start+size-1]
                ans=max(ans,n)
                
        return ans 
        '''
        #solution2
        for i in range(1,len(nums)):
            #adding prev elm to curr elms
            nums[i]=max(nums[i-1]+nums[i],nums[i])
        return max(nums)
            
