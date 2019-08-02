'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        while matrix:
            #appending first row of matrix to ans
            ans.extend(list(matrix.pop(0)))
             #reversing remaining rows and taking transpose of obtained matrix
            matrix=zip(*[i[::-1] for i in matrix])
        return ans
            
            

        
        
