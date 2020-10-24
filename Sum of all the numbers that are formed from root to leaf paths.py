'''
Given a binary tree, where every node value is a Digit from 1-9 .Find the sum of all the numbers which are formed from root to leaf paths.
For example consider the following Binary Tree.

           6
       /      \
     3          5
   /   \          \
  2     5          4  
      /   \
     7     4
  There are 4 leaves, hence 4 root to leaf paths:
   Path                    Number
  6->3->2                   632
  6->3->5->7               6357
  6->3->5->4               6354
  6->5>4                    654   
Answer = 632 + 6357 + 6354 + 654 = 13997 

idea: The idea is to do a preorder traversal of the tree. In the preorder traversal, keep track of the value calculated till the current node, let this value be val. For every node, 
we update the val as val*10 plus node’s data.

'''
def treePathsSumUtil(root, val): 
  
    # Base Case 
    if root is None: 
        return 0
  
    # Update val 
    val = (val*10 + root.data) 
  
    # If current node is leaf, return the current value of val 
    if root.left is None and root.right is None: 
        return val 
  
    # Recur sum of values for left and right subtree 
    return (treePathsSumUtil(root.left, val) + 
            treePathsSumUtil(root.right, val)) 
