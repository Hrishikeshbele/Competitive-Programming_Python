'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

'''
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def helper(root,ans,s):
            s=s+str(root.val)
            if root.left:
                helper(root.left,ans,s+'->')
            if root.right:
                helper(root.right,ans,s+'->')
            if not root.left and not root.right:
                ans.append((s))
            return ans
        if not root:
            return []
        return helper(root,[],'')
       
