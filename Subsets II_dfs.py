'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

Idea:

dfs(nums = [1,2,2], path = [], res = [])
|
|__ dfs(nums = [2,2] , path = [1], res = [[]])
|    |__ dfs(nums = [2] , path = [1,2], res = [[],[1]])
|    	  |__ dfs(nums = [] , path = [1,2,2], res = [[],[1], [1,2]])
|    	  	   # next: res = [[],[1],[1,2],[1,2,2]]
|    	  	   # for loop will not be executed
	 
|__ dfs(nums = [2] , path = [[2]], res = [[],[1],[1,2],[1,2,2]])
|    |__ dfs(nums = [] , path = [[2,2]], res = [[],[1],[1,2],[1,2,2],[2])
|    	  	   # next iteration: res =  [[],[1],[1,2],[1,2,2],[2],[2,2])
|    	  	   # for loop will not be executed
|
|for there two cases we skip the iteration to avoid generate duplicate subsets using continue .
| dfs(nums =[2, 2] , path =[1],res =  [[], [1], [1, 2], [1, 2, 2]])  
| dfs( nums =[1, 2, 2] , path =[] ,res = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]) 

if 2 consecative elements are same then we just do it for one of 2 elements because we will be doing duplicate work if we do it for  2 elms.The inner loop will process the first "1," 
then skip the next "1's". for example nums[1,1] and path=[2] then if we proceed with this pair will will get 2 same subsets i.e. [[2,1] ,[2,1]] .
why sorting?: because the input might contain duplicates, after sorting, duplicated number will be next to each other, this way this duplication check nums[i] == nums[i-1] will work.
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        self.helper(nums,[],res)
        return res
    def helper(self,nums,path,res):
        res.append(path)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.helper(nums[i+1:],path+[nums[i]],res)
        

