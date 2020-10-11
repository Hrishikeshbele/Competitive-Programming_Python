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
    
# solution 2 (2 pointers)

'''
 The first step remain same. The idea for second step is take two index variables i and j, initialize them as 0 and 1 respectively. Now run a linear loop. 
 If arr[j] – arr[i] is smaller than n, we need to look for greater arr[j], so increment j. If arr[j] – arr[i] is greater than n, we need to look for greater arr[i], 
 so increment i. 
 '''
def findPair(arr,n): 
    arr=sorted(arr)
    size = len(arr) 
  
    # Initialize positions of two elements 
    i,j = 0,1
  
    # Search for a pair 
    while i < size and j < size: 
        if i != j and arr[j]-arr[i] == n: 
            return True
        elif arr[j] - arr[i] < n: 
            j+=1
        else: 
            i+=1
    
    return False
