'''
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
head = [4,5,1,9], 
Input: node = 5(only that perticular node is given)
Output: [4,1,9]
'''
#idea here make curr node node.next bypass copy 

def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next
