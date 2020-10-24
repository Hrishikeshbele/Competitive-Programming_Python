'''
Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Input: root1 = [1,2], root2 = [2,2]
Output: true

approach : we find root nodes of both tree and compare them

'''


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def leafs(root):
            if root:
                if not root.left and not root.right:
                    return [root.val]
                return leafs(root.left)+leafs(root.right)
            else:
                return []
        return leafs(root1)==leafs(root2)
        
