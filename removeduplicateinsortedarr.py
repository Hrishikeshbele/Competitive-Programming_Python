'''
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].

'''

def removeDuplicates( A):
        n = len(A)
        if n <= 1:
            return n
        size = n
        j = 1
        prev = A[0]
        #we are accumelating first occurance of all the elm's to right side
        #we are using j to keep track of right side elm
        #[0,0,1,1,1,2,2,3,3,4] -> [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
        for i in range(j,n):
            #junction where next elm starts ex 1,2
            if A[i] != prev:
                prev = A[i]
                #assigning curr elm to right side
                A[j] = A[i]
                j += 1
                
        return j
