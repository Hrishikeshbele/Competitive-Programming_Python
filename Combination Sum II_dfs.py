'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

idea is same as combination sum 1 we just add one statement to avoid duplicates.if 2 consecative elements are same then we just do it for one of 2 elements because we will be 
doing duplicate work if we do it for  2 elms.
'''

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        cand=sorted(candidates)
        self.helper(cand,target,0,[],res)
        return res
    
    def helper(self,cand,target,ind,path,res):
        if target==0:
            res.append(path)
            return
        if target<0:
            return 
        for i in range(ind,len(cand)): 
            if i>ind and cand[i]==cand[i-1]:
                continue
            self.helper(cand,target-cand[i],i+1,path+[cand[i]],res)
        
        
