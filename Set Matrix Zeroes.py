'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

solution approach: 1st we create set of all rows and columns where value 0 is present then we make elements in these rows and columns zero.
'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zeroRows = set()
        zeroCols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)
        
        for row in zeroRows:
            matrix[row][:] = map(lambda x:0, matrix[row])
        
        for i in range(len(matrix)):
            for col in zeroCols:
                matrix[i][col] = 0
