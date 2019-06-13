'''
Given a collection of integers that might contain duplicates, S, return all possible subsets.
Example :
If S = [1,2,2], the solution is:

[[],
[1],
[1,2],
[1,2,2],
[2],
[2, 2]]
'''
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        #intialising res to store the result
        res = [[]]
        #sorting the list before we proceed since since we have to return result in
        # lexicographical order and we will use sorted list while comparing elms
        S.sort()
        for i in range(len(S)):
            #if curr elm is first elm of list or if last elm is not equal
            #to curr elm then assign len of res to k var
            if i==0 or S[i]!=S[i-1]:
                k=len(res)
            #here we add curr elm to prev elm in list if not repeated if repeated
            #we just need to add curr to elm of prev s[i-1]
            for j in range(len(res)-k,len(res)):
                res.append(res[j]+[S[i]])
        res.sort()
        return res
