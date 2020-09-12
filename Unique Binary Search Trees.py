'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
   idea here is calculate possible no of trees for each no from 1 to n and add them.for calculating max no of trees multiply possible no of trees for its immediate neighbours.
    ex for n=3: res[3] = res[0]*res[2]+res[1]*res[1]+res[2]*res[0] .
  '''
  
  class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=[0 for i in range(n+1)]
        ans[0]=1
        for j in range(1,n+1):
            #multiplying each no with its immediate neigbours
            for i in range(j):
                ans[j]+=ans[i]*ans[j-i-1]
        return ans[-1]
