'''
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
'''



class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #base case1-if root is not there return true
        if not root:
            return True
        #bc2- if left root exist and val at left != val at root return false
        if root.left :
            if root.val!=root.left.val:
                return False
        #bc3-same as base case 3
        if root.right:
            if root.val!=root.right.val:
                return False
        #if both left and right subtree returned true then returns true and vice-versa
        return self.isUnivalTree(root.right) and self.isUnivalTree(root.left)
