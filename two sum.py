'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
solution idea: maintain values and indices of previous elms.for every new elm check if tar-num has already been found.if yes return their 
indices else store these values in dictonary for further use.
time:O(n)
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index={}  #key is num and value is index on num
        for i,num in enumerate(nums):
            #check if tar-num is already there in dict keys
            if target-num in num_to_index:
                return [num_to_index[target-num],i]
            num_to_index[num]=i
        return []
        
        
        
    
