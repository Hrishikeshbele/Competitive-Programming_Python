'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

idea: main idea here is similar to unique path one solution but instead of initialising all elements of 1st row and column to 1 we set them equal to zero if we enconter obstacle before
that element else to 1 and zero for obstacle element. for rest of matrix we follow same logic.

'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
    
        m = obstacleGrid
        if not m or m == [[]] or len(m)==0 or m[0][0] == 1:
            return 0
        
        # start:
        m[0][0] = 1
        
        # top row:
        for i in range(1, len(m[0])):
            if m[0][i] == 1: # obstacle
                m[0][i] = 0
            else:
                m[0][i] = m[0][i-1] # previous cell (cell to the left)
                
        # left most col:
        for i in range(1, len(m)):
            if m[i][0] == 1: # obstacle
                m[i][0] = 0
            else:
                m[i][0] = m[i-1][0] # previous cell (cell to the top)
                
        # rest of the grid:
        for i in range(1, len(m)):
            for j in range(1, len(m[0])):
                if m[i][j] == 1:
                    m[i][j] = 0
                else:
                    m[i][j] = m[i-1][j] + m[i][j-1]
                    
        return m[len(m)-1][len(m[0])-1]
