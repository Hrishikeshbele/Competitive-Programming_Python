'''
Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
input :
A : [1 5 3]
k : 2
Output :
1

'''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        #storing elm in dict for efecting checking 
        dict={}
        for num in A:
            #if there is any elm in dict such that i+-B == elm then we found pair
            if dict.get(num+B,False) or dict.get(num-B,False):
                return 1
            #storing elm as key and its value is set to true
            dict[num]=True
        return 0
    
