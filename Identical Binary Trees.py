'''
Given two binary trees, write a function to check if they are equal or not.
'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        #base case-1
        if A is None and B is None:
            return 1
        #base case-2
        if not A or not B:
            return 0
        else:
            #checking recursively if value at both tree is same or not.
            return int(A.val==B.val and self.isSameTree(A.left,B.left) and self.isSameTree(A.right,B.right))
        return 0
