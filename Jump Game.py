'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

idea: here idea is we keep the count of maximum number reachable at each elment.if at any element we find that maximum reachable element is less than current index means we can't 
reach the end index of list so we return false. if we find no such elements then we return true. 
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # m represent the maximum index we can reach currently
        m=0
        for i in range(len(nums)):
            # maximum index reachable is less than last index
            if i>m:
                return False
            m=max(m,i+nums[i])
            
        return True
            
                
                
            
        
        
