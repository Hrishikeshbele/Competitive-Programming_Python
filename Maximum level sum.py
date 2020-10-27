'''
Problem Description

Given a Binary Tree denoted by root node A having integer value on nodes. You need to find maximum sum level in it.

Example Input
Input 1:

 Tree:      4
          /   \
         2     5
        / \   / \
       1  3  2   6
       
   Output 1:

 12
 
 Explanation 1:

 Sum of all nodes of 0'th level is 4 
 Sum of all nodes of 1'th level is 7
 Sum of all nodes of 2'th level is 12
 Hence maximum sum is 12
 
 we find sum of elm at each level by level order transversal and then return max of them.
 
 '''
 
 class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        ans=[]
        nex=[A]
        while A and nex:
            temp=[]
            lev=[] # we can use var also insted of list and add val each time at pert level 
            for n in nex:
                lev.append(n.val)
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            ans.append(sum(lev))
            nex=temp
            
        return max(ans)
            
