'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #we initialise the first row and column to 1 so that we can use forward tracking and since there is only 1 path to reach them.
        count=[[1 for i in range(m) ] for j in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                count[i][j]=count[i][j-1]+count[i-1][j]
        return count[n-1][m-1]
                

        
