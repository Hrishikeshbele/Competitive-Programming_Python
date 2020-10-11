'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

idea : watch this video by TECH DOSE-> https://www.youtube.com/watch?v=7IQHYbmuoVU
here we do dfs using backtracking

'''

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        self.helper(range(1,n+1),k,0,[],res)
        return res #backtracking
    
    def helper(self,n,k,ind,path,res):
        if k==0:
            res.append(path)
            return 
        for i in range(ind,len(n)):
            self.helper(n,k-1,i+1,path+[n[i]],res)
      
