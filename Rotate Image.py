'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

here idea is to first create rows of output matrix by picking ith column and reversing it. then we assing these rows to original matrix.
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #create list of output matrix rows
        lst2=[]
        for j in range(len(matrix)):
            lst2.append([item[j] for item in matrix][::-1])
        #replace rows in matrix with above rows
        for i in range(len(lst2)):
            matrix[i]=lst2[i]
            
        return matrix
            
                
                    
        
