'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers.
Example: 
given array S = {-1 2 1 -4}, 
and target = 1.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer (target)
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        closest = None
        for i in range(len(A) - 2):
            j, k = i + 1, len(A) - 1
            while k > j:
                threeSum = A[i] + A[j] + A[k]
                if threeSum == B:
                    return threeSum
                #checking if diff between curr threesum and target is less then diff between target and closest(closest sum to target until now) we 
                # replace closest with threesum
                if closest is None or abs(B - threeSum) < abs(B - closest):
                    closest = threeSum
                if threeSum < B:
                    j += 1
                else:
                    k -= 1
        return closest

