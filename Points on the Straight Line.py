'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Sample Input :
(1, 1)
(2, 2)
Sample Output :
2 
'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        n = len(A)
        #if len(A)<=2 then return n
        if (n<=2):
            return n
        m = 0 #result value
        for i in range(n):
            l = {}  #every time reset the dict
            dup = 1 #count the duplicates
            for j in range(n):
                if (A[i]==A[j] and B[i]==B[j] and i!=j):        
                    dup+=1  #count duplicates
                elif i!=j :
                    if (A[i]==A[j]):  #vertical line
                        #we are increamenting value of key 'v' for every verical pt
                        l['v'] = l.get('v',0) + 1
                    elif (B[i]==B[j]): # horizontal line
                        l['h'] = l.get('h',0) + 1
                    else:   #regular slope
                        slope = 1.0*(B[i]-B[j])/(A[i]-A[j])
                        l[slope] = l.get(slope,0)+1
            if (len(l)>0): 
                m = max(m,max(l.values())+dup)
            else: #if all points are duplicates, l is empty.
                m = max(m,dup)
        return m

            
