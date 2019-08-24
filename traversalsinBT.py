'''
how to perform different transversal in BT
'''
def preorder(root):
  return [root.val] + preorder(root.left) + preorder(root.right) if root else []
# go to the left and run the function again,when there's no left, add value to the list.
def inorder(root):
  return  inorder(root.left) + [root.val] + inorder(root.right) if root else []
def postorder(root):
  return  postorder(root.left) + postorder(root.right) + [root.val] if root else []
