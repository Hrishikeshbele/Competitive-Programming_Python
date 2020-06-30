'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Idea: watch this video -> https://www.youtube.com/watch?v=KukNnoN-SoY
at each iteration we remove perticular no from list to create list of  possible nos and add it to path. then we recurrece with same logic on this list of possible nos.
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.helper(nums,[],res)
        return res
    
    def helper(self,nums,path,res):
        if not nums:
            res.append(path)
            return 
        for i in range(len(nums)):
            self.helper(nums[:i]+nums[i+1:],path+[nums[i]],res)
