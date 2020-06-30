'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

we used concept of backtracking to solve this problem .detailed explaination is given below.

dfs(nums = [1,2,3], path = [], res = [])
|
|__ dfs(nums = [2,3] , path = [1], res = [[]])
|    |__ dfs(nums = [3] , path = [1,2], res = [[],[1]])
|    	  |__ dfs(nums = [] , path = [1,2,3], res = [[],[1], [1,2]])
|    	  	   # next: res = [[],[1],[1,2],[1,2,3]]
|    	  	   # for loop will not be executed
|
|__ dfs(nums = [3] , path = [[2]], res = [[],[1],[1,2],[1,2,3]])
|    |__ dfs(nums = [] , path = [[2,3]], res = [[],[1],[1,2],[1,2,3],[2])
|    	  	   # next iteration: res =  [[],[1],[1,2],[1,2,3],[2],[2,3])
|    	  	   # for loop will not be executed
|
|__ dfs(nums = [], path = [[3]], res =  [[],[1],[1,2],[1,2,3],[2],[2,3])
     	  	   # next iteration: res =  [[],[1],[1,2],[1,2,3],[2],[2,3],[3])
     	  	   # for loop will not be executed
             
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.helper(nums,[],res)
        return res
    def helper(self,nums,path,res):
        res.append(path)
        for i in range(len(nums)):
            self.helper(nums[i+1:],path+[nums[i]],res)
