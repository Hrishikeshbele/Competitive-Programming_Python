'''
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
'''
#first we find sum of first row and first column since only way to go to next elm here is from prev elm.and then we sum other min sum
#elemnts

def minPathSum(self, A):
        # The first row can only be the result of moving to the right
        for i in range(1, len(A[0])):
            A[0][i] += A[0][i-1]
        # The first column can only be the result of moving down  
        for i in range(1, len(A)):
            A[i][0] += A[i-1][0]
        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                A[i][j] += min(A[i-1][j], A[i][j-1])
        return A[-1][-1]
        
        
        
