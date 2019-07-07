'''
There are N Mice and N holes are placed in a straight line. 
Each hole can accomodate only 1 mouse. 
A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x − 1. Any of these moves consumes 1 minute.
Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.
'''
#basic idea here is to sort the both arrays so that we get minimum distance for each mice
#solution1
def mice(self, A, B):
        A.sort()
        B.sort()
        dist = [abs(a-b) for a,b in zip(A,B)]
        return max(dist)
#solution2
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        res=[]
        A.sort()
        B.sort()
        maxx = -9999999
        for i in range(len(A)) :
            maxx = max(maxx, abs(A[i]-B[i]))
        
        return maxx

