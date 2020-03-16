'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

solution approach: we first add 1 to new row then we consider two list seperately one containing all elm of prev list except first elm and
other all elms except last elm then we will add corresponding elms of these lists and append them to curr row after which we add 1 at end.
now we append this new row to our output list.

'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        ans=[[1]]
        for i in range(1,numRows):
            #first we append new row with 1
            ans.append([1])
            #then we add intermediate elms using last row 
            for num1,num2 in zip(ans[-2][:-1],ans[-2][1:]):
                ans[-1].append(num1+num2)
            #then at last we append 1 to row
            ans[-1].append(1)
        return ans
                
                
            
        
