'''
Given a string, find the rank of the string amongst its permutations sorted lexicographically. 
Assume that no characters are repeated.

Example :

Input : 'acb'
Output : 2
'''

class Solution:
    def findRank(self, A):
        alphabet = sorted(A)
        ans = 0
        #rank = number of characters less than first character * (N-1)! + rank of permutation of string with the first character removed
        for i,x in enumerate(A):
            ans += alphabet.index(x) * math.factorial(len(A) - i - 1)
            alphabet.remove(x)
        return (ans + 1) % 1000003
