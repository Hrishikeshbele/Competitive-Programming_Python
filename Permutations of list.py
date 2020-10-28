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
------------
#second solution 
# idea: permutation [a,b,c,...] = [a + permutation[b,c,...], b + permutation[a,c,..], ...]

def permutations(s):
    ans=[]
    #base case
    if len(s)==1:
        return [s]
    for a in s:
        #list of elm except a 
        remaining=[x for x in s if x!=a]
        #list of all possible permutations of remaining elm list
        perm=permutations(remaining)
        #adding each elm of perm with curr elm a and then append it to ans 
        for j in perm:
            ans.append([a]+j)
    return ans

# backtracking solution

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
