'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
Given A : [1, 2, 3]
A height balanced BST  : 

      2
    /   \
   1     3

'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if not A:
            return None
        #finding middle of array
        mid=len(A)/2
        #assigning middle to root of array
        root=TreeNode(A[mid])
        #doing same thing for left half and right half
        root.left=self.sortedArrayToBST(A[:mid])
        root.right=self.sortedArrayToBST(A[mid+1:])
        
        return root
