'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
'''
def sortedSquares(self, A):
        
        """
        :type A: List[int]
        :rtype: List[int]
        """
        '''  
        #solution1
        sqr=[x**2 for x in A]
        return sorted(sqr)
        '''
        #solution2
        def absv(x):
            return abs(x)
        return [x**2 for x in sorted(A,key=absv)]
