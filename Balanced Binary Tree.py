'''
Given a binary tree, determine if it is height-balanced.

solution: helper function height return height of tree. tree is balanced if left and right subtrees are balanced and difference height of
left and right subtree is not greater than 1.
'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    #function to find height of binary tree
    def height(self,root):
            if root is None:
                return 0
            return  1+max(self.height(root.left),self.height(root.right)) #1 for root node
    #function to check if binary tree is balanced   
    def isBalanced(self, A):
       #base case
       if A is None:
           return int(True)
       #checking if 3 conditions satisfy.
       return int(self.isBalanced( A.right) and self.isBalanced( A.left) and abs(self.height(A.left)-self.height(A.right))<=1)
       
        
