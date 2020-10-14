'''
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:

Input: N = 2, K = 1
Output: 0

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001

for approach watch youtube video of aditya verma . k before mid will be same as previous row and for k values after mid elm are revese of first half of prev row.

'''
class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if n==1 and k==1:
            return 0
        mid=2**(n-1)//2 # Total no of item in level n : 2**(n-1)
        if k<=mid:
            return self.kthGrammar(n-1,k)
        else:
            return 1- self.kthGrammar(n-1,k-mid)
        
