'''
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value.
Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.
'''

'''
idea-we use recursion here with the base case stating that when values are equal return the root tree.else we compare it with root node 
value, if value is greater then we search in right subtree else we search in left subtree
'''


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root:
            if root.val==val:
                return root
            elif  root.val<val:
                return self.searchBST( root.right, val)
            elif  root.val>val:
                return self.searchBST( root.left, val)
        return None
        
            
        
