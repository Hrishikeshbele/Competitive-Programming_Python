'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

idea here is very simple first we do inorder traversal and get the node values. note that since we are doing inorder traverasal we should get sorted list. we check in returned list if 
prev elm is greater than or equal to current elm then we say tree is not valid.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #doing preorder traversal and getting ordered list
        def preorder(root,trav):
            if root:
                preorder(root.left,trav)
                trav.append(root.val)
                preorder(root.right,trav)
    
            return trav
        #checking if tree is valid
        rut=preorder(root,[])
        for i in range(len(rut)-1):
            if rut[i]>=rut[i+1]:
                return False
        return True
    
