'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        self.helper(nums,[],res)
        return (res)
    
    def helper(self,nums,path,res):
        if not nums :
            res.append(path)
            return 
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.helper(nums[:i]+nums[i+1:],path+[nums[i]],res)
