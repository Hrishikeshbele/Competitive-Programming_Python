'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
solution idea:we first append root node to queue then append its value to level then dequeue it to check if it has left and right node resp if it has 
then we append them to queue and dequeue one by one reapeating above process.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue=[]
        ans=[]
        if not root:
            return root
        #append root node in queue
        queue.append(root)
        while queue:
            level=[]
            for _ in range(len(queue)):
                #taking elm from start of queue
                node=queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        return reversed(ans)
        
            
        
        
