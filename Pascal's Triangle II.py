'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
Example:

Input: 3
Output: [1,3,3,1]

solution approach:see the solution of pascal's triangle_1.
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans=[[1]]
        if rowIndex==0:
            return [1]
        for i in range(1,rowIndex+1):
            ans.append([1])
            for n1,n2 in zip(ans[-2][:-1],ans[-2][1:]):
                ans[-1].append(n1+n2)
            ans[-1].append(1)
        return ans[-1]
            
        
