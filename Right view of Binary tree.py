'''
Problem Description

Given a binary tree A of integers. Return an array of integers representing the right view of the Binary tree.

Right view of a Binary Tree: is a set of nodes visible when the tree is visited from Right side.
Input 1:

        1
      /   \
     2    3
    / \  / \
   4   5 6  7
  /
 8 
 Output 1:

 [1, 3, 7, 8]
 
 idea here is we do level order transversal and append last elm at each level.
 '''
 
 class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        nex=[A]
        ans=[]
        while A and nex:
            temp=[]
            lev=[]
            for n in nex:
                lev.append(n.val)
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            ans.append(lev[-1])
            nex=temp
        return ans
