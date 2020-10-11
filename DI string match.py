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
ex.
suppose S.length = 4 and S="IDID", so the numbers we need to fill in the result set is 0 1 2 3 4
if the current char is 'I', we want to pick a number in the current potential options (0-4) that satisfies all scenarios in next loop, it should be the smallest one, which is 0
now the rest of options are 1 2 3 4
if the current char is 'D', again, we want to make sure that FOR EVERY NUMBER WE PICK IN NEXT ROUND will satisfy a[current] > a[current+1], then pick the largest value in 1 2 3 4, which is 4
then set becomes [1 2 3], we repeat the above
the thinking is really similar to "greedy" that we pick some number that can most satisfy the cases for next loop
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
        
# solution 2 ( same idea as above solution)

def diStringMatch(self, S):
    """
    :type S: str
    :rtype: List[int]
    """
    c1=[i for i in range(len(S)+1)]
    c2=c1[::-1]
    ans=[]
    for elm in S:
        if elm=='I':
            ans.append(c1.pop(0))
        elif elm=='D':
            ans.append(c2.pop(0))
    ans.append(c1.pop(0))
    return ans
