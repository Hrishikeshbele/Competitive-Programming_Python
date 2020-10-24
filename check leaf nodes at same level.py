'''
Given a Binary Tree, check if all leaves are at same level or not.
          12
        /    \
      5       7       
    /          \ 
   3            1
  Leaves are at same level

          12
        /    \
      5       7       
    /          
   3          
   Leaves are Not at same level
   
   
 idea:
 The idea is to first find level of the leftmost leaf and store it in a variable leafLevel. Then compare level of all other leaves with leafLevel, if same,
 return true, else return false. We traverse the given Binary Tree in Preorder fashion. An argument leaflevel is passed to all calls. The value of leafLevel is initialized
 as 0 to indicate that the first leaf is not yet seen yet. The value is updated when we find first leaf. Level of subsequent leaves (in preorder) is compared with leafLevel.
 
 '''
 
 class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.leaflevel=0
        def leafs(root,level):
            if not root :
                return True
            if root:
                if not root.left and not root.right:
                    # When a leaf node is found first time 
                    if self.leaflevel ==0 :
                        self.leaflevel=level # Set first leaf found
                        return True
                    # If this is not first leaf node, compare its level 
                    # with first leaf's level 
                    return self.leaflevel==level
            # If this is not first leaf node, compare its level 
            # with first leaf's level
            return leafs(root.left,level+1) and leafs(root.right,level+1)
