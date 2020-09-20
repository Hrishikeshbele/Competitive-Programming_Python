'''
Problem Description

Given a string A consisting only of '(' and ')'.

You need to find whether parantheses in A is balanced or not ,if it is balanced then return 1 else return 0.

Example Input
Input 1:

 A = "(()())"
Input 2:

 A = "(()"


Example Output
Output 1:

 1
Output 2:

 0
 
 idea to solve the problem is simple we append each opening parathesis and pop when we encounter closing parathesis. if while poping we found that there no opening parthesis for 
 current closing parathesis i.e list is empty we return 0 . at last we check if list is empty we return 0 else 1.
 
 '''
 
 class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        ans=[]
        for i in A:
            if i=='(':
                ans.append('(')
            elif i==')':
                if ans:
                    ans.pop()
                else:
                    return 0
        if ans:
            return 0
        return 1
