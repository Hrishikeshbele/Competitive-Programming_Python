'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

idea here is we do dfs by adding list elm one at time and see if their sum equals to target if yes we append them to ans else we backtrack.
watch this video: https://www.youtube.com/watch?v=irFtGMLbf-s
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        '''
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        '''
        candidates.sort()
        res =[]
       
        def re_sum(candidates,target,index,comb,res):
            if target==0:
                res.append(comb)
                return 
            elif target<0:
                return 
            
            for i in range(index,len(candidates)):
                re_sum(candidates,target-candidates[i],i,comb+[candidates[i]],res)
                
        re_sum(candidates,target,0,[],res)
        
        return res
                
            
            
            
        
        
        
