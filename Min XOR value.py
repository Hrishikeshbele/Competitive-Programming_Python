'''
Given an array of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.
Examples : 
Input 
0 2 5 7 
Output 
2 
'''
class Solution:
    # @param A : list of integers
    # @return: an integer
    def findMinXor(self, a):
        #sorting array to reduce computation
        a.sort()
        n=len(a)
        #intialising ans to large positive value
        ans=10**10
        for i in range(1,n):
            if ans>a[i-1] ^ a[i]:
                ans=a[i-1] ^ a[i]
                #since we know that xor can't be less than 0 due to given constraints
                if ans == 0: 
                    return ans
        return ans
