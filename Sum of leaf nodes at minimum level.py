'''
Given a binary tree containing n nodes. The problem is to get the sum of all the leaf nodes which are at minimum level in the binary tree.

Examples:

Input : 
              1
            /   \
           2     3
         /  \   /  \
        4   5   6   7
           /     \
          8       9

Output : 11
Leaf nodes 4 and 7 are at minimum level.
Their sum = (4 + 7) = 11. 

approach: using level order transversal and flag var . we intialise flag var with False value and as we encounter 1st leaf node we make flag var True indicating we have reached 
minimum level. we take sum of leaf nodes at that level.

'''
class Solution(object):
    def levelordtranv(self,root):
        level=[root]
        sm=0
        flag=False
        while level and not flag:
            nxt=[]
            for node in level:
                if not node.left and not node.right:
                    sm+=node.val
                    flag=True
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            level=nxt
        return sm
 
