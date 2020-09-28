'''
given a binary tree return all path from root node to leaf node

we use the concept of dfs. we go further down the tree add that node to our curr list and if we reach the leaf node we append that as one path in our ans list.

'''
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans=[]
        def helper(root,curr):
            # if curr node is not present retrieve back 
            if not root:
                return
             #if we heat at leaf node. append the path upto and retrive back 
            if not root.left and not root.right:
                ans.append(curr+[root.val])
                return
            helper(root.left,curr+[root.val])
            helper(root.right,curr+[root.val])
        if not root:
            return []
        helper(root,[])
        return ans
