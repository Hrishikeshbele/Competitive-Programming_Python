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

approach is same as permutation 1 but here we skipped the iteration where two consecutive no  in a list are same.The inner loop will process the first "1," then skip the next "1's".if 2 consecative elements are same then we just do it for one
of 2 elements because we will be doing duplicate work if we do it for  2 elms.for example nums[1,1] and path=[2] then if we proceed with this pair will will get 2 same subsets i.e. [[2,1] ,[2,1]]
why sorting?: because the input might contain duplicates, after sorting, duplicated number will be next to each other, this way this duplication check nums[i] == nums[i-1] will work

Given the input of [1, 1, 2], at the first stage, we have 2 choices to pick a number as the first number in the final permutation, i.e. 1 and 2. Suppose that we pick the number
1, now the remaining numbers would become [1, 2]. Note: The reason that we have only 2 choices instead of 3, is that there is a duplicate in the given input. Picking any of the 
duplicate numbers as the first number of the permutation would lead us to the same permutation at the end.At the second stage, we now then have again 2 choices, i.e. [1, 2]. Let 
us pick again the number 1, which leaves us the only remaining number 2.Now at the third stage, we have only one candidate number left, i.e. [2]. We then pick the last remaining
number, which leads to a final permutation sequence of [1, 1, 2].
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
