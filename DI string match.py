'''
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]

soltn idea: append elm from left side if I occures and form right side for D.ex. for I start from 0 and for D start from 4 then next time
if I come append 1 and 3 for D
'''

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans=[]
        right=len(S)
        left=0
        for i in range(len(S)):
            if S[i]=='I':
                ans.append(left)
                left+=1
            else:
                ans.append(right)
                right-=1
        #appending remaining last element
        ans.append(right)
                 
        return ans
        
