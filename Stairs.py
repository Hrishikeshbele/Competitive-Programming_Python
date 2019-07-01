'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top
'''
#solution based of fact that The person can reach n’th stair from either (n-1)'th stair or from (n-2)'th stair.
# ways(n) = ways(n-1) + ways(n-2)

class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, n):
      #base case
        if n == 1:
            return 1
        res = [0]*n
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]
        
 
