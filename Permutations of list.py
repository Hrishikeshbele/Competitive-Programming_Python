'''
Given a collection of numbers, return all possible permutations.
[1,2,3] will have the following permutations:
[[1,2,3]
[1,3,2]
[2,1,3] 
[2,3,1] 
[3,1,2] 
[3,2,1]]
'''

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, nums):
	    n = len(nums)
	    #creating ans to store all perms
        ans=[]
        #base case 
        if n == 0 : return [[]]
        for idx,val in enumerate(nums):
            #finding permutation of all remaining no's except curr one
            other_pert=self.permute(nums[:idx]+nums[idx+1:])
            #mapping each value in other_pert using lambda function to 
            #generate permutations for curr no
            ans += map(lambda perm:[val]+perm,other_pert)
            
        return ans
