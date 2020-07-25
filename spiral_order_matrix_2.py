'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Given n = 3,

You should return the following matrix:

[
  [ 1, 2, 3 ],
  [ 8, 9, 4 ],
  [ 7, 6, 5 ]
]
'''
def generateMatrix(self, n):
    A, lo = [], n*n+1
    while lo > 1:
        lo, hi = lo - len(A), lo
        A = [range(lo, hi)] + zip(*A[::-1])
    return A
  
#SOLUTION 2
''' 
(1) Create a matrix to store the coordinates

(0,0) (0,1) (0,2)

(1,0) (1,1) (1,2)

(2,0) (2,1) (2,2)

(2) Read it out using the trick of "Spiral Matrix I"

(0,0) (0,1) (0,2) (1,2) (2,2) ...

trick: 
before zip(*cord)[::-1] : [[(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)]]
after zip(*cord)[::-1]: [((1, 2), (2, 2)), ((1, 1), (2, 1)), ((1, 0), (2, 0))]

(3) Put 1, 2, 3, ... n**2 at these coordinates sequentially. Done.

idea here is to get the index in spiral traversal manner.
'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[[0 for i in range(n)] for k in range(n)]
        cord=[[(i,j) for j in range(n)] for i in range(n)]
        count=1
        while cord:
            for x,y in cord.pop(0):
                ans[x][y]=count
                count+=1
            cord=zip(*cord)[::-1]
        return ans
            
        
'''
Solution 3

here we maintain 4 var left,right,top,down. we first go from left to right assigning num.after this operation we decrease the top by 1 to indicate that operation for 1st row is done.
then we go down in last column assigning num and here we decrese the right var to indicate last column is done .similary then we go from right to left and down to top.
'''
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []
        ans=[[0 for i in range(n)] for k in range(n)]
        left,right,top,down,num =0,n-1,0,n-1,1
        while left<=right and top<=down:
            for i in range(left,right+1):
                ans[top][i]=num
                num+=1
            top+=1
            for i in range(top,down+1):
                ans[i][right]=num
                num+=1
            right-=1
            for i in range(right,left-1,-1):
                ans[down][i]=num
                num+=1
            down-=1
            for i in range(down,top-1,-1):
                ans[i][left]=num
                num+=1
            left+=1
        return ans
                
            
        
