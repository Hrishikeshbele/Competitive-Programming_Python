'''
Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:1
'''
# idea here is to increament the interator of arr in which min curr min elm is present this will lead us to find min diff . since smaller elm and larger elms will have greater
# difference than 2 larger elms. so we increment the smaller counter to find next bigger elm. 
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        a, b, c = 0, 0, 0
        mini = int(1e9)
        while (a < len(A)) & (b < len(B)) & (c < len(C)):
            #finding the max and min num amongs three
            maxx, minn = max(A[a], B[b], C[c]), min(A[a], B[b], C[c])
            #if curr diff is smaller than min update minn
            if abs(maxx - minn) < mini:
                mini = abs(maxx - minn)
            #checking for min elm is present in which arr of 3,increment the iterator for that arr only
            if minn == A[a]:
                a += 1
            elif minn == B[b]:
                b += 1
            else:
                c += 1
        return mini
   

# solution 2 

'''
same approach but with largest element instead of smallest elm.In every step, the only possible way to decrease the difference is to decrease the maximum element out of 
the three elements.So traverse to the next largest element in the array containing the maximum element for this step and update the answer variable.
'''

def solve(A, B, C): 
  
        # assigning the length -1 value 
        # to each of three variables 
        i = len(A) - 1
        j = len(B) - 1
        k = len(C) - 1
  
        # calculating min difference  
        # from last index of lists 
        min_diff = abs(max(A[i], B[j], C[k]) -
        min(A[i], B[j], C[k])) 
  
        while i != -1 and j != -1 and k != -1: 
            current_diff = abs(max(A[i], B[j],  
            C[k]) - min(A[i], B[j], C[k])) 
  
            # checking condition 
            if current_diff < min_diff: 
                min_diff = current_diff 
  
            # calculating max term from list 
            max_term = max(A[i], B[j], C[k]) 
  
            # Moving to smaller value in the 
            # array with maximum out of three. 
            if A[i] == max_term: 
                i -= 1
            elif B[j] == max_term: 
                j -= 1
            else: 
                k -= 1
        return min_diff 
