'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2] ]
  
  here we used 3 sum concept and modified it for 4sum problem.
  '''
  
  class Solution(object):
    def fourSum(self, a, t):
        a = sorted(a)
        n = len(a)
        ans = set()
        #iteration through list until n-3 indicating there are 2 pointers ahead of index i
        # i indicates the index of 1st elm
        for i in range(n-3):
            #j indicates index of 2nd elm 
            for j in range(i+1, n-2):
                #target to be searched as 2 sum in list 
                rem = t - a[i] - a[j]
                #setting left and right indexes for 2 pointer search
                l, r = j+1, n-1
                while l < r:
                    if a[l] + a[r] == rem:
                        ans.add(tuple([a[i], a[j], a[l], a[r]]))
                        l += 1
                        r-=1
                    elif a[l] + a[r] < rem:
                        l+= 1
                    else: 
                        r -= 1
        return sorted([list(x) for x in ans])
