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
            if abs(maxx - minn) < mini:
                mini = abs(maxx - minn)
            if minn == A[a]:
                a += 1
            elif minn == B[b]:
                b += 1
            else:
                c += 1
        return mini
