'''
Given an integer n, return any array containing n unique integers such that they add up to 0.
solution approach:start with -(n-1) and append the integer with gap of 2 upto n.which eventually will give us array whose sum is 0.
'''

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return range(1-n,n,2)

# solution2 
'''
Explanation:
First, take a look at a few examples:

n = 1: ans = [0]
n = 2: ans = [-1,1]
n = 3: ans = [-1,0,1]
n = 4: ans = [-2,-1,1,2]
n = 5: ans = [-2,-1,0,1,2]
So, we should return an array where the values are symmetric.
If n%2 is not equal to zero (n is odd), we append 0 to the answer list.
So, we use a for loop; and each time we add -i and i to the answer list.

'''

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        if n%2==0:# n is even
            for i in range(1,(n/2)+1): # we iterate n/2 +1 times
                ans.extend([i,-i])
        else: # n is odd
            for i in range(1,(n//2)+1):
                ans.extend([i,-i])
            ans.append(0)
        return ans
