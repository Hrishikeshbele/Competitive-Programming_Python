'''
897. Increasing Order Search Tree
Easy

332

335

Favorite

Share
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
   '''
   
   class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #wefirst append all nodes in 1 list in inordertraversal order
        def inordertrans(root):
            pre=[]
            if root:
                return inordertrans(root.left)+[root.val]+inordertrans(root.right)
            else:
                return []
        #getting all nodes in inorder transversal order
        nodes=inordertrans(root)
        #storing first node
        new_node=TreeNode(nodes[0])
        #creating node using which we will iterate 
        node=new_node
        #iterating over list of nodes and everytime assign node to the right of paremt node
        #and advencing node to right child
        for i in range(1,len(nodes)):
            node.right=TreeNode(nodes[i])
            node=node.right
        #returing root node
        return new_node
        
            
        
