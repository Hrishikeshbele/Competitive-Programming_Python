'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

solution approach: Idea here is simple smallest element from up and left of current element will be added to current element . we will do this for whole matrix and then we will 
return last element of matrix which is nothing but smallest path sum.

'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #cumm sum of 1st column
        for i in range(1,len(grid)):
            grid[i][0]+=grid[i-1][0]
        #cumm sum of 1st row
        for i in range(1,len(grid[0])):
            grid[0][i]+=grid[0][i-1]
        #cumm sum for rest of matrix
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j]+=min(grid[i][j-1],grid[i-1][j])
        return grid[-1][-1]
